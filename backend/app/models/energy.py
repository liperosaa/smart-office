from sqlalchemy import Column, Integer, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.sql import func

from app.database.base import Base


class EnergyRecord(Base):
    __tablename__ = "energy_records"

    id = Column(Integer, primary_key=True, index=True)

    equipment_id = Column(
        Integer,
        ForeignKey("equipments.id"),
        nullable=False
    )

    consumo_watts = Column(Float, nullable=False)

    temperatura = Column(Float, nullable=False)

    ligado = Column(Boolean, default=True)

    criado_em = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )