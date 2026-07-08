from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.connection import get_database

from app.schemas.room_schema import (
    RoomCreate,
    RoomResponse
)

from app.services.room_service import (
    create_room,
    get_rooms
)


router = APIRouter(
    prefix="/rooms",
    tags=["Rooms"]
)



@router.post(
    "/",
    response_model=RoomResponse
)
def create(
    room: RoomCreate,
    db: Session = Depends(get_database)
):

    return create_room(
        db,
        room
    )



@router.get(
    "/",
    response_model=list[RoomResponse]
)
def list_rooms(
    db: Session = Depends(get_database)
):

    return get_rooms(db)