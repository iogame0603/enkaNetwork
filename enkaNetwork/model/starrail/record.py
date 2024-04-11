from pydantic import BaseModel

class ChallengeInfo(BaseModel):
    scheduleMaxLevel: int
    scheduleGroupId: int
    noneScheduleMaxLevel: int

class RecordInfo(BaseModel):
    equipmentCount: int
    maxRogueChallengeScore: int
    avatarCount: int
    achievementCount: int
    challengeInfo: ChallengeInfo