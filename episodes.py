from fastapi import APIRouter
from services.simpsons_service import fetch

# Router responsável pelos episódios
router = APIRouter(
    prefix="/episodes",
    tags=["Episodes"]
)

@router.get("")
def get_episodes(
    limit: int = 10,          # Limite de episódios retornados
    name: str | None = None   # Filtro opcional pelo nome do episódio
):
    """
    Lista episódios dos Simpsons.
    Permite filtro por nome e controle de limite.
    """
    # Consome a API externa usando a camada de serviço
    return fetch(
        "episodes",
        {
            "limit": limit,
            "name": name
        }
    )
