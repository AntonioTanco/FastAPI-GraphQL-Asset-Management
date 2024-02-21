from RedisCache import Cache
from typing import List
from StrawberryGQL.asset_utils import AssetType
import json

def get_assets() -> List[AssetType]:
    data = Cache.r.get('assets')

    if data is not None:
        # Deserialize the data from JSON
        assets = [AssetType(**item) for item in json.loads(data)]
        return assets
    
    else:
        return []