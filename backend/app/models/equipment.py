from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from app.database.base import Base


class Equipment(Base):

    __tablename__ = "equipments"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    nome = Column(
        String,
        nullable=False
    )


    categoria = Column(
        String,
        nullable=False
    )


    consumo_watts = Column(
        Integer,
        nullable=False
    )


    ligado = Column(
        Boolean,
        default=False
    )


    room_id = Column(
        Integer,
        ForeignKey("rooms.id"),
        nullable=False
    )