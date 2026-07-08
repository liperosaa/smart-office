from pydantic import BaseModel


class DailyReportResponse(BaseModel):
    data: str
    consumo_total: float
    equipamentos_monitorados: int



class MonthlyReportResponse(BaseModel):
    mes: str
    consumo_total: float
    media_diaria: float