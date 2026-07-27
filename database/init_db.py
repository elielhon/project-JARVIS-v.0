from database.database import engine
from database import models


print("Criando banco...")

models.Base.metadata.create_all(
    bind=engine
)

print("Banco criado com sucesso!")