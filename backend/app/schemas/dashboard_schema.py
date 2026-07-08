from pydantic import BaseModel


class DashboardResponse(BaseModel):
    usuarios: int
    salas: int
    equipamentos: int
    consumo_total: float