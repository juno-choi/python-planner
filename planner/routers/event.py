from fastapi import APIRouter, Body, HTTPException, status
from planner.models.event import Event
from typing import List

event_router = APIRouter(tags=["Events"])

events = []

@event_router.get("/", response_model=List[Event])
async def getAll() -> List[Event]:
    return events

@event_router.get("/{id}", response_model=Event)
async def get(id: int) -> Event:
    for event in events:
        if event.id == id:
            return event
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="id가 유효하지 않습니다."
    )

@event_router.post("/")
async def post(body: Event = Body(...)) -> dict:
    events.append(body)
    return {
        "message" : "등록 성공"
    }

@event_router.delete("/")
async def delete() -> dict:
    events.clear()
    return {
        "message" : "삭제 성공"
    }

@event_router.delete("/{id}")
async def deleteId(id: int) -> dict:
    for event in events:
        if event.id == id:
            events.remove(event)
            return {
                "message" : "삭제 성공"
            }
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="id가 유효하지 않습니다."
    )
