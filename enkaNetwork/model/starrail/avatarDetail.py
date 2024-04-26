from pydantic import BaseModel, Field
from typing import List

from .skillTree import SkillTree
from .equipment import Equipment
from .relic import Relic
from ...util import HonkaiStarrailUtil

class AvatarDetail(BaseModel):
    avatarId: int
    name: str
    level: int
    icon: str
    element: str
    baseType: str
    rarity: int

    skillTreeList: List[SkillTree]

    equipment: Equipment = None
    relicList: List[Relic] = []

    def __init__(self, **data):
        avatarInfo = HonkaiStarrailUtil.get_avatar_info(data["avatarId"])
        data["name"] = avatarInfo["name"]
        data["element"] = avatarInfo["element"]
        data["baseType"] = avatarInfo["avatarBaseType"]
        data["rarity"] = avatarInfo["rarity"]
        data["icon"] = avatarInfo["cutinFrontImg"]

        super().__init__(**data)