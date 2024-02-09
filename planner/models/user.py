from pydantic import BaseModel
from typing import Optional, List
from planner.models.event import Event

class User(BaseModel):
    email: str
    password: str
    events: Optional[List[Event]]

    class Config:
        json_schema_extra= {
            "example": {
                "email" : "email@mail.com",
                "password": "password",
                "events": []
            }
        }

class UserSignIn(BaseModel):
    email: str
    password: str

    class Config:
        json_schema_extra= {
            "example": {
                "email" : "email@mail.com",
                "password": "password"
            }
        }