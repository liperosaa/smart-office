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

from app.services.energy_service import (
    create_energy_record,
    get_energy_records,
    get_energy_summary
)

from app.schemas.energy_summary_schema import EnergySummaryResponse

from app.schemas.ranking_schema import EnergyRankingResponse

from app.services.energy_service import (
    get_energy_ranking
)

from app.services.energy_service import filter_energy

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

@router.get(
    "/summary/",
    response_model=EnergySummaryResponse
)
def summary(
    db: Session = Depends(get_db)
):
    return get_energy_summary(db)

@router.get(
    "/ranking/",
    response_model=list[EnergyRankingResponse]
)
def ranking(
    db: Session = Depends(get_db)
):
    return get_energy_ranking(db)

@router.get("/filter/")
def filter_records(
    equipment_id: int | None = None,
    ligado: bool | None = None,
    min_consumo: float | None = None,
    db: Session = Depends(get_db)
):

    return filter_energy(
        db,
        equipment_id,
        ligado,
        min_consumo
    )