from sqlalchemy.orm import Session

from app.models.room import Room
from app.schemas.room_schema import RoomCreate



def create_room(
    db: Session,
    room: RoomCreate
):

    new_room = Room(
        nome=room.nome,
        tipo=room.tipo,
        capacidade=room.capacidade,
        andar=room.andar
    )


    db.add(new_room)
    db.commit()
    db.refresh(new_room)


    return new_room



def get_rooms(
    db: Session
):

    return db.query(Room).all()