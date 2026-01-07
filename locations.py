from fastapi import APIRouter
from services.simpsons_service import fetch

# Router responsável pelas localizações
router = APIRouter(
    prefix="/locations",   # Prefixo correto para localizações
    tags=["Locations"]
)

@router.get("")
def get_locations(
    limit: int = 10,          # Limite de registros retornados
    name: str | None = None   # Filtro opcional por nome da localização
):
    """
    Lista localizações dos Simpsons.
    Permite filtro por nome e controle de limite.
    """
    # Chamada centralizada para a API externa
    return fetch(
        "locations",
        {
            "limit": limit,
            "name": name
        }
    )
