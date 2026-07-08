from pydantic import BaseModel


class GeneralReportResponse(BaseModel):
    total_usuarios: int
    total_salas: int
    total_equipamentos: int
    consumo_total: float



class EquipmentReportResponse(BaseModel):
    equipamento: str
    consumo_total: float



class RoomReportResponse(BaseModel):
    sala: str
    consumo_total: float



class MonthlyReportResponse(BaseModel):
    mes: str
    consumo_total: float