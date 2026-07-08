from app.database.connection import engine
from app.database.base import Base

from app.models import User


print("Criando tabelas...")

Base.metadata.create_all(bind=engine)

print("Banco criado com sucesso!")