from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    nome = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(100),
        unique=True,
        nullable=False
    )

    senha_hash = Column(
        String(255),
        nullable=False
    )

    cargo = Column(
        String(50),
        nullable=False
    )

    ativo = Column(
        Boolean,
        default=True,
        nullable=False
    )

    criado_em = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )