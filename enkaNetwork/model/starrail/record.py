from pydantic import BaseModel
from typing import Optional

class ChallengeInfo(BaseModel):
    scheduleMaxLevel: int = None
    scheduleGroupId: int = None
    noneScheduleMaxLevel: int = None

class RecordInfo(BaseModel):
    equipmentCount: int
    maxRogueChallengeScore: int = 0
    avatarCount: int
    achievementCount: int
    challengeInfo: Optional[ChallengeInfo]
    
    def __init__(self, **data):
        super().__init__(**data)