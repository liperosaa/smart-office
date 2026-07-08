from sqlalchemy import Column, Integer, String, Boolean

from app.database.base import Base


class Room(Base):

    __tablename__ = "rooms"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    nome = Column(
        String,
        nullable=False
    )


    tipo = Column(
        String,
        nullable=False
    )


    capacidade = Column(
        Integer,
        nullable=False
    )


    andar = Column(
        Integer,
        nullable=False
    )


    ativo = Column(
        Boolean,
        default=True
    )