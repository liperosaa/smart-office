from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_database

from app.schemas.equipment_schema import (
    EquipmentCreate,
    EquipmentResponse
)

from app.services.equipment_service import (
    create_equipment,
    get_equipments
)


router = APIRouter(
    prefix="/equipments",
    tags=["Equipments"]
)



@router.post(
    "/",
    response_model=EquipmentResponse
)
def create(
    equipment: EquipmentCreate,
    db: Session = Depends(get_database)
):

    return create_equipment(
        db,
        equipment
    )



@router.get(
    "/",
    response_model=list[EquipmentResponse]
)
def list_equipment(
    db: Session = Depends(get_database)
):

    return get_equipments(db)