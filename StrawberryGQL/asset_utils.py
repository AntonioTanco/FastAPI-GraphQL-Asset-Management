import strawberry
from typing import List

@strawberry.type
class AssetType:
    id: str
    hostname: str
    description: str
    serial_number: str

def create_asset_objects(assets: List[dict]) -> List[AssetType]:
    return [AssetType(**asset) for asset in assets]