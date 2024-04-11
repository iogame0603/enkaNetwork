from pydantic import BaseModel, field_validator, ValidationInfo
from typing import List, Union

from ...util import HonkaiStarrailUtil

class Prop(BaseModel):
    type: str
    value: Union[int, float]

    @field_validator("value")
    def v(cls, value: Union[int, float], values: ValidationInfo):
        # import math

        # if "Delta" in values.data["type"]:
        #     return int(math.floor(value))
        # return round(value * 100, 1)
        pass
    
    def __init__(self, **data):
        data["type"] = HonkaiStarrailUtil.get_localizations(data["type"])
        super().__init__(**data)

class EquipFlat(BaseModel):
    props: List[Prop]
    name: int

class RelicFlat(BaseModel):
    setName: str
    props: List[Prop]

    def __init__(self, **data):
        data["setName"] = HonkaiStarrailUtil.get_localizations(data["setName"])
        super().__init__(**data)