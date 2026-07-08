from pydantic import BaseModel


class UserCreate(BaseModel):

    nome: str
    email: str
    senha: str
    cargo: str


class UserResponse(BaseModel):

    id: int
    nome: str
    email: str
    cargo: str
    ativo: bool

    class Config:
        from_attributes = True