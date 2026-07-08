from pydantic import BaseModel


class EquipmentCreate(BaseModel):

    nome: str
    categoria: str
    consumo_watts: int
    ligado: bool = False
    room_id: int



class EquipmentResponse(EquipmentCreate):

    id: int


    class Config:
        from_attributes = True