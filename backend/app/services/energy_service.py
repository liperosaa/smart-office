from sqlalchemy.orm import Session

from app.models.energy import EnergyRecord
from app.schemas.energy_schema import EnergyCreate

from sqlalchemy import func

from app.models.energy import EnergyRecord


from sqlalchemy import func

from app.models.energy import EnergyRecord
from app.models.equipment import Equipment




def create_energy_record(
    db: Session,
    energy: EnergyCreate
):
    novo = EnergyRecord(**energy.model_dump())

    db.add(novo)
    db.commit()
    db.refresh(novo)

    return novo


def get_energy_records(db: Session):
    return db.query(EnergyRecord).all()
def get_energy_summary(db):

    media = db.query(
        func.avg(EnergyRecord.consumo_watts)
    ).scalar()

    maior = db.query(
        func.max(EnergyRecord.consumo_watts)
    ).scalar()

    menor = db.query(
        func.min(EnergyRecord.consumo_watts)
    ).scalar()


    return {
        "media_consumo": media or 0,
        "maior_consumo": maior or 0,
        "menor_consumo": menor or 0
    }

def get_energy_ranking(db):

    resultado = (
        db.query(
            Equipment.nome,
            func.sum(EnergyRecord.consumo_watts)
        )
        .join(
            EnergyRecord,
            Equipment.id == EnergyRecord.equipment_id
        )
        .group_by(
            Equipment.nome
        )
        .order_by(
            func.sum(EnergyRecord.consumo_watts).desc()
        )
        .all()
    )


    ranking = []

    for equipamento, consumo in resultado:
        ranking.append(
            {
                "equipamento": equipamento,
                "consumo_total": consumo
            }
        )

    return ranking

def filter_energy(
    db,
    equipment_id=None,
    ligado=None,
    min_consumo=None
):

    query = db.query(EnergyRecord)


    if equipment_id:
        query = query.filter(
            EnergyRecord.equipment_id == equipment_id
        )


    if ligado is not None:
        query = query.filter(
            EnergyRecord.ligado == ligado
        )


    if min_consumo:
        query = query.filter(
            EnergyRecord.consumo_watts >= min_consumo
        )


    return query.all()