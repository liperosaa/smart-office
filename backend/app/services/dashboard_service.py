from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.user import User
from app.models.room import Room
from app.models.equipment import Equipment
from app.models.energy import EnergyRecord


def get_dashboard(db: Session):

    usuarios = db.query(User).count()

    salas = db.query(Room).count()

    equipamentos = db.query(Equipment).count()

    consumo = db.query(
        func.sum(EnergyRecord.consumo_watts)
    ).scalar()

    if consumo is None:
        consumo = 0

    return {
        "usuarios": usuarios,
        "salas": salas,
        "equipamentos": equipamentos,
        "consumo_total": consumo
    }

def test_dashboard(client):

    response = client.get(
        "/dashboard/"
    )

    assert response.status_code == 200