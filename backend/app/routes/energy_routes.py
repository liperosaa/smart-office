from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.energy_schema import (
    EnergyCreate,
    EnergyResponse
)
from app.services.energy_service import (
    create_energy_record,
    get_energy_records
)

router = APIRouter(
    prefix="/energy",
    tags=["Energy"]
)


@router.post("/", response_model=EnergyResponse)
def create(
    energy: EnergyCreate,
    db: Session = Depends(get_db)
):
    return create_energy_record(db, energy)


@router.get("/", response_model=list[EnergyResponse])
def list_all(
    db: Session = Depends(get_db)
):
    return get_energy_records(db)