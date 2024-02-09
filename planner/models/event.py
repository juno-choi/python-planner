from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        json_schema_extra = {
            "example" : {
                "title": "제목",
                "image": "https://linktomyimage.com/image.png",
                "description": "설명~~~",
                "tags": ["태그1", "태그2", "태그3"],
                "location" : "kakao"
            }
        }