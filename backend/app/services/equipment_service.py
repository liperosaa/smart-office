from sqlalchemy.orm import Session

from app.models.equipment import Equipment
from app.schemas.equipment_schema import EquipmentCreate



def create_equipment(
    db: Session,
    equipment: EquipmentCreate
):

    new_equipment = Equipment(
        nome=equipment.nome,
        categoria=equipment.categoria,
        consumo_watts=equipment.consumo_watts,
        ligado=equipment.ligado,
        room_id=equipment.room_id
    )


    db.add(new_equipment)
    db.commit()
    db.refresh(new_equipment)


    return new_equipment



def get_equipments(
    db: Session
):

    return db.query(Equipment).all()