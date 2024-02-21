from pydantic import BaseModel

class AssetModel(BaseModel):
    hostname: str
    description: str
    serial_number: str