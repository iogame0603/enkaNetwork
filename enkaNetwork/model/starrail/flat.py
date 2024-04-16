from pydantic import BaseModel, field_validator, ValidationInfo
from typing import List, Union

from ...util import HonkaiStarrailUtil

class BasePropValue(BaseModel):
    type: str

    def __init__(self, **data):
        data["type"] = HonkaiStarrailUtil.get_localizations(data["type"])
        super().__init__(**data)

class DeltaValue(BasePropValue):
    value: Union[int, float]

    @field_validator("value")
    def validator_value(cls, value: Union[int, float]):
        return int(round(value))

    class Config:
        validate_assignment = True

class PercentValue(BasePropValue):
    value: float

    @field_validator("value")
    def validator_value(cls, value: float):
        return round(value * 100, 1)

    def value2percent(self):
        return f"{self.value}%"

    class Config:
        validate_assignment = True

class Prop(BaseModel):
    propValue: Union[DeltaValue, PercentValue]

    def __init__(self, **data):
        if data["type"].find("Delta") != -1:
            data["propValue"] = DeltaValue(**data)
        else:
            data["propValue"] = PercentValue(**data)
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