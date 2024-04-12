from pydantic import BaseModel, field_validator, ValidationInfo
from typing import List, Union

from ...util import HonkaiStarrailUtil

class Prop(BaseModel):
    type: str
    value: Union[int, float]

    def __init__(self, **data):
        if data["type"].find("Delta") != -1:
            data["value"] = int(round(data["value"]))
        else:
            data["value"] = round(data["value"] * 100, 1)
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