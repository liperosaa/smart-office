from sqlalchemy.orm import Session

from app.models.energy import EnergyRecord
from app.schemas.energy_schema import EnergyCreate


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