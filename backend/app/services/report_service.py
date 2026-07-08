from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.user import User
from app.models.room import Room
from app.models.equipment import Equipment
from app.models.energy import EnergyRecord


def get_general_report(db: Session):

    total_users = db.query(
        func.count(User.id)
    ).scalar()


    total_rooms = db.query(
        func.count(Room.id)
    ).scalar()


    total_equipment = db.query(
        func.count(Equipment.id)
    ).scalar()


    total_consumption = db.query(
        func.sum(EnergyRecord.consumo_watts)
    ).scalar()


    return {
        "total_usuarios": total_users or 0,
        "total_salas": total_rooms or 0,
        "total_equipamentos": total_equipment or 0,
        "consumo_total": total_consumption or 0
    }



def get_equipment_report(db: Session):

    result = (
        db.query(
            Equipment.nome,
            func.sum(EnergyRecord.consumo_watts)
            .label("consumo_total")
        )
        .join(
            EnergyRecord,
            Equipment.id == EnergyRecord.equipment_id
        )
        .group_by(
            Equipment.nome
        )
        .all()
    )


    return [
        {
            "equipamento": item.nome,
            "consumo_total": item.consumo_total
        }
        for item in result
    ]



def get_room_report(db: Session):

    result = (
        db.query(
            Room.nome,
            func.sum(EnergyRecord.consumo_watts)
            .label("consumo_total")
        )
        .join(
            Equipment,
            Room.id == Equipment.room_id
        )
        .join(
            EnergyRecord,
            Equipment.id == EnergyRecord.equipment_id
        )
        .group_by(
            Room.nome
        )
        .all()
    )


    return [
        {
            "sala": item.nome,
            "consumo_total": item.consumo_total
        }
        for item in result
    ]

def test_general_report(client):

    response = client.get(
        "/reports/general"
    )

    assert response.status_code == 200