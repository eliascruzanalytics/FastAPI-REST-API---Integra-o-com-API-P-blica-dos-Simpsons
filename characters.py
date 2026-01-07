# Importa o APIRouter para criação de rotas modulares
from fastapi import APIRouter

# Importa a função fetch responsável por consumir a API externa
from services.simpsons_service import fetch

# Cria um router específico para personagens
router = APIRouter(
    prefix="/characters",  # Prefixo das rotas
    tags=["Characters"]    # Tag exibida no Swagger
)

@router.get("")
def get_characters(
    limit: int = 10,          # Quantidade máxima de registros retornados
    name: str | None = None   # Filtro opcional por nome do personagem
):
    """
    Lista personagens dos Simpsons.
    Permite filtro por nome e controle de limite.
    """
    # Chama a API externa passando os parâmetros como query params
    return fetch(
        "characters",
        {
            "limit": limit,
            "name": name
        }
    )
