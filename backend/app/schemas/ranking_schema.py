from pydantic import BaseModel


class EnergyRankingResponse(BaseModel):
    equipamento: str
    consumo_total: float