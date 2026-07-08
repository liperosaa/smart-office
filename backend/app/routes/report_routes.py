from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db

from app.schemas.report_schema import (
    GeneralReportResponse,
    EquipmentReportResponse,
    RoomReportResponse
)

from app.services.report_service import (
    get_general_report,
    get_equipment_report,
    get_room_report
)


router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get(
    "/general",
    response_model=GeneralReportResponse
)
def general_report(
    db: Session = Depends(get_db)
):
    return get_general_report(db)



@router.get(
    "/equipment",
    response_model=list[EquipmentReportResponse]
)
def equipment_report(
    db: Session = Depends(get_db)
):
    return get_equipment_report(db)



@router.get(
    "/rooms",
    response_model=list[RoomReportResponse]
)
def rooms_report(
    db: Session = Depends(get_db)
):
    return get_room_report(db)