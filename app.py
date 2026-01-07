# Importa a classe FastAPI, responsável por criar a aplicação
from fastapi import FastAPI

# Importa os routers de cada domínio da API
from routers.characters import router as characters_router
from routers.episodes import router as episodes_router
from routers.locations import router as locations_router

# Cria a instância principal da aplicação FastAPI
app = FastAPI(
    title="The Simpsons API - FastAPI Portfolio",  # Título exibido no Swagger
    description="API em FastAPI consumindo a The Simpsons API pública",  # Descrição da API
    version="1.0.0"  # Versão da aplicação
)

# Registra o router de personagens na aplicação
app.include_router(characters_router)

# Registra o router de episódios na aplicação
app.include_router(episodes_router)

# Registra o router de localizações na aplicação
app.include_router(locations_router)
