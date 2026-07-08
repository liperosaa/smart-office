from pydantic import BaseModel


class EnergySummaryResponse(BaseModel):
    media_consumo: float
    maior_consumo: float
    menor_consumo: float