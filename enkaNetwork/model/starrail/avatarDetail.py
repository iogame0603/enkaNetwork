from pydantic import BaseModel
from typing import List

from .skillTree import SkillTree
from .equipment import Equipment
from .relic import Relic
from ...util import HonkaiStarrailUtil

class AvatarDetail(BaseModel):
    name: str
    level: int
    icon: str
    element: str
    baseType: str
    rarity: int

    skillTreeList: List[SkillTree]

    equipment: Equipment
    relicList: List[Relic]

    # TODO : add icon

    def __init__(self, **data):
        avatarInfo = HonkaiStarrailUtil.get_avatar_info(data["avatarId"])
        data["name"] = avatarInfo["name"]
        data["element"] = avatarInfo["element"]
        data["baseType"] = avatarInfo["avatarBaseType"]
        data["rarity"] = avatarInfo["rarity"]
        data["icon"] = avatarInfo["cutinFrontImg"]

        super().__init__(**data)