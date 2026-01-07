# Biblioteca usada para realizar requisições HTTP
import requests

# URL base da API pública dos Simpsons
BASE_URL = "https://thesimpsonsapi.com/api"

# Tempo máximo de espera por resposta da API externa (em segundos)
TIMEOUT = 10

def fetch(endpoint: str, params: dict | None = None):
    """
    Função responsável por consumir a API externa dos Simpsons.

    :param endpoint: recurso da API (characters, episodes, locations)
    :param params: parâmetros opcionais da requisição (query params)
    :return: resposta da API em formato JSON
    """

    # Realiza a requisição GET para a API externa
    response = requests.get(
        f"{BASE_URL}/{endpoint}",  # Monta a URL final
        params=params,             # Parâmetros enviados na query string
        timeout=TIMEOUT            # Timeout de segurança
    )

    # Lança uma exceção caso a resposta não seja 200 (OK)
    response.raise_for_status()

    # Retorna o conteúdo da resposta em JSON
    return response.json()
