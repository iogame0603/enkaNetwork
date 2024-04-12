from pydantic import BaseModel, Field

from .flat import EquipFlat
from ...util import HonkaiStarrailUtil

class Equipment(BaseModel):
    name: str
    level: int
    # promotion: int
    rank: int
    flat: EquipFlat = Field(alias="_flat")

    icon: str
    rarity: int

    def __init__(self, **data):
        weaponInfo = HonkaiStarrailUtil.get_weapon_info(data["tid"])
        data["name"] = weaponInfo["name"]
        data["icon"] = weaponInfo["icon"]
        data["rarity"] = weaponInfo["rarity"]
        super().__init__(**data)