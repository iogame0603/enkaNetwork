from pydantic import BaseModel

class SkillTree(BaseModel):
    pointId: int
    level: int