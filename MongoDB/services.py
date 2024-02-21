from typing import List

def individual_serial(asset) -> dict:
        return {
            "id": str(asset["_id"]),
            "hostname" : asset.get("hostname"),
            "description" : asset.get("description"),
            "serial_number": asset["serial_number"]
        }
    
def list_serial(assets) -> list:
    return[individual_serial(asset) for asset in assets]