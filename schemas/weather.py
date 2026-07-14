from pydantic import BaseModel ,Field
from typing import Optional


class WeatherRequestModel(BaseModel):
    city:str
    temperature:float
    condition:str
    humidity:int
    wind_speed:int
    country:str
    created_by:str
    admin_note:str

class CreateUpdateModel(BaseModel):
    city:str=Field(
        title="city name",
        description="enter your city name",
        max_length=20,
        min_length=1,
    )
    temperature:float=Field(
        ge=0,
        gt=100,
        title="Set temperature",
        description="anyalsis the temperature",
    )
    condition:str=Field(
        max_length=10,
        min_length=1,
    )
    humidity:int=Field(
        ge=0,
        le=100,
    )
    wind_speed:int=Field(
        ge=0,
        le=50,
    )
    country:str=Field(
        max_length=10,
        min_length=1,
        title="country name",
        description="enter your country name",
    )
    created_by:str=Field(
        max_length=30,
        min_length=1,
    )
    admin_note:str=Field(
        max_length=40,
        min_length=1,
        title="admin note",
        description="enter a note about weather",
    )

    

class UpdateRequestModel(BaseModel):
    city:Optional[str]|None=Field(
        title="city name",
        description="enter your city name",
        max_length=20,
        min_length=1,
    )
    temperature:Optional[float]|None=Field(
        ge=0,
        le=100,
        title="Set temperature",
        description="anyalsis the temperature",
    )
    condition:Optional[str]|None=Field(
        max_length=10,
        min_length=1,
    )
    humidity:Optional[int]|None=Field(
        ge=0,
        le=100,
    )
    wind_speed:Optional[int]|None=Field(
        ge=0,
        le=50,
    )
    country:Optional[str]|None=Field(
       max_length=10,
       min_length=1,
       title="country name",
       description="enter your country name",
    )
    created_by:Optional[str]|None=Field(
         max_length=30,
        min_length=1,
    )
    admin_note:Optional[str]|None=Field(
        max_length=40,
        min_length=1,
        title="admin note",
        description="enter a note about weather",
    )


class ResponseModel(BaseModel):
    city:str
    temperature:float
    condition:str
    humidity:int
    wind_speed:int
    country:str