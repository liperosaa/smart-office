from pydantic import BaseModel


class RoomCreate(BaseModel):

    nome: str
    tipo: str
    capacidade: int
    andar: int



class RoomResponse(RoomCreate):

    id: int
    ativo: bool


    class Config:
        from_attributes = True