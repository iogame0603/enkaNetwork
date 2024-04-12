from pydantic import BaseModel, Field

from .flat import RelicFlat
from ...util import HonkaiStarrailUtil

class SubAffix(BaseModel):
    affixId: int
    cnt: int
    step: int

class Relic(BaseModel):
    icon: str
    level: int = None
    type: int

    rarity: int
    # mainAffixId: int
    # subAffixList: List[SubAffix]

    flat: RelicFlat = Field(alias="_flat")

    def __init__(self, **data):
        relicInfo = HonkaiStarrailUtil.get_relic_info(data["tid"])
        data["icon"] = relicInfo["icon"]
        data["rarity"] = relicInfo["rarity"]
        super().__init__(**data)