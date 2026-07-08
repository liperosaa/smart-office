from datetime import datetime

from pydantic import BaseModel


class EnergyCreate(BaseModel):
    equipment_id: int
    consumo_watts: float
    temperatura: float
    ligado: bool


class EnergyResponse(BaseModel):
    id: int
    equipment_id: int
    consumo_watts: float
    temperatura: float
    ligado: bool
    criado_em: datetime

    model_config = {
        "from_attributes": True
    }