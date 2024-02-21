import strawberry
import json

from typing import List, Optional
from MongoDB import NoSQL
from MongoDB.assets import AssetModel
from MongoDB.services import list_serial
from StrawberryGQL.asset_utils import AssetType
from RedisCache import Cache
from logger import logger
mongoDB = NoSQL()

# @strawberry.type
# class AssetType:
#     id: str
#     hostname: str
#     description: str
#     serial_number: str

@strawberry.type
class Query:

    @strawberry.field
    def assets(self, info) -> List[AssetType]:

        data = Cache.r.get('assets')
        
        if data is not None:

        # Deserialize the data from JSON
            print("Assets were found in Redis, serving asset data from Redis instead.")
            assets = [AssetType(**item) for item in json.loads(data)]
            return assets
        
        assets_cursor = mongoDB.asset_collection.find()
        assets = list_serial(assets_cursor)

        if assets is not None:

        # Serialize the assets to JSON and store in Redis
            Cache.r.set('assets', json.dumps([dict(**assets) for assets in assets]))
            print("Assets were fetched from MongoDB, redis cache has been updated!")

            return [AssetType(**asset) for asset in assets]
    
    @strawberry.field
    def asset_by_hostname(self, info, hostname: str) -> Optional[AssetType]:

        # Try to get the data from Redis
        data = Cache.r.get('assets')

        #Checks if data is cached in Redis
        if data is not None:

            # Deserialize the data from JSON
            assets = [AssetType(**item) for item in json.loads(data)]

            #Loops through assets and checks if that asset.hostname matches our query
            for asset in assets:
                if asset.hostname == hostname:

                    #returns that asset
                    return asset

        # If the data is not in Redis, get it from MongoDB
        asset = mongoDB.asset_collection.find_one({"hostname": hostname})

        #Checks if that asset exist in MongoDB
        if asset is not None:

            # Convert the MongoDB document to a pydantic AssetModel instance
            asset = AssetModel(**asset)

            # Add the asset to Redis
            Cache.r.set('asset:' + hostname, json.dumps(asset.model_dump()))
            return asset

        return None
    
    @strawberry.field
    def asset_by_serialnumber(self, info, serialnumber: str) -> Optional[AssetType]:
        # Try to get the data from Redis
        data = Cache.r.get('assets')

        #Checks if data is cached in Redis
        if data is not None:

            # Deserialize the data from JSON
            assets = [AssetType(**item) for item in json.loads(data)]

            #Loops through assets and checks if that asset.hostname matches our query
            for asset in assets:
                if asset.serial_number == serialnumber:

                    #returns that asset
                    return asset

        # If the data is not in Redis, get it from MongoDB
        asset = mongoDB.asset_collection.find_one({"serial_number": serialnumber})

        #Checks if that asset exist in MongoDB
        if asset is not None:
            
            # Convert the MongoDB document to a pydantic AssetModel instance
            asset = AssetModel(**asset)

            # Add the asset to Redis
            Cache.r.set('asset:' + serialnumber, json.dumps(asset.model_dump()))
            return asset
        
        return None
    
@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_asset(self, info, hostname: str, description: str, serial: str) -> AssetType:
        asset_data = AssetModel(hostname=hostname, description=description, serial_number=serial)
        result = mongoDB.asset_collection.insert_one(asset_data.model_dump())
        new_asset = mongoDB.asset_collection.find_one({"_id": result.inserted_id})
        
        #Clears Redis Cache
        Cache.r.delete('assets')

        logger.info(f'An Asset was successfully created: {new_asset["hostname"]}')

        return AssetType(id=str(new_asset["_id"]), hostname=new_asset["hostname"], serial_number=new_asset["serial_number"], description=new_asset["description"])
    

    @strawberry.mutation
    def remove_asset_by_id(self, info, id: str) -> bool:
        
        result = mongoDB.asset_collection.delete_one({"_id": id})

        # Invalidate the cache in Redis
        Cache.r.delete('assets')
        print("Redis cache has been cleared!")

        # Return True if an asset was deleted, False otherwise
        return result.deleted_count > 0
    
    @strawberry.mutation
    def remove_asset_by_hostname(self, info, hostname: str) -> bool:

        result = mongoDB.asset_collection.delete_one({"hostname": hostname})

        # Invalidate the cache in Redis
        Cache.r.delete('assets')
        print("Redis cache has been cleared!")

        # Return True if an asset was deleted, False otherwise
        return result.deleted_count > 0
    
schema = strawberry.Schema(query=Query, mutation=Mutation)