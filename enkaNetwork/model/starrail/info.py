from pydantic import BaseModel, Field
from typing import List

from .avatarDetail import AvatarDetail
from .record import RecordInfo
from ...util import HonkaiStarrailUtil

class DetailInfo(BaseModel):
    nickname: str
    signature: str = ""
    uid: int
    headIcon: str
    level: int
    worldLevel: int = 0
    platform: str = ""

    avatarInfoList: List[AvatarDetail] = Field(alias="avatarDetailList")
    recordInfo: RecordInfo

    def __init__(self, **data):
        data["headIcon"] = HonkaiStarrailUtil.get_head_icon(data["headIcon"])
        super().__init__(**data)