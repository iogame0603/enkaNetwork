from pydantic import BaseModel

from ...util import HonkaiStarrailUtil

class SkillTree(BaseModel):
    icon: str
    pointType: int
    level: int

    def __init__(self, **data):
        skillTreeInfo = HonkaiStarrailUtil.get_skilltree_info(data["pointId"])
        data["icon"] = skillTreeInfo["icon"]
        data["pointType"] = skillTreeInfo["pointType"]
        super().__init__(**data)