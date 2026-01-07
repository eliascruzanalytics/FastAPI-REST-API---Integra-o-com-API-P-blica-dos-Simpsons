<img width="983" height="333" alt="image" src="https://github.com/user-attachments/assets/2ad95540-291b-4a9d-96ab-2db7c6f5b6a5" />


# FastAPI REST API — Integração com The Simpsons API

API REST desenvolvida em Python com FastAPI, consumindo dados de uma API pública dos Simpsons.
O projeto tem foco didático e de portfólio, demonstrando organização de código, boas práticas e testes via Swagger.

Objetivo 
- Demonstrar a criação de uma API REST do zero com FastAPI
- Aplicar organização modular usada no mercado
- Consumir uma API externa simulando uma camada de dados
- Facilitar testes através da documentação automática

Conceitos Abordados

- API REST e HTTP
- FastAPI e tipagem de dados
- Rotas e Query Params
- Integração com API externa
- Documentação automática (Swagger / OpenAPI)


Estrutura das pastas no projeto
```API_PYTHON/
├── app.py
├── requirements.txt
├── routers/
│   ├── __init__.py
│   ├── characters.py
│   ├── episodes.py
│   └── locations.py
└── services/
    ├── __init__.py
    └── simpsons_service.py
```

Descrição rápida:

- app.py → inicializa a aplicação
- routers/ → definição das rotas da API
- services/ → consumo da API externa
- requirements.txt → dependências do projeto

Tecnologias Utilizadas

- Python
- FastAPI
- Uvicorn
- Requests

Instalação

```pip install -r requirements.txt```

Executando o Projeto
```uvicorn app:app --reload```

A API estará disponível em:
http://127.0.0.1:8000

Endpoints Disponíveis

| Método | Rota          | Descrição          |
| ------ | ------------- | ------------------ |
| GET    | `/characters` | Lista personagens  |
| GET    | `/episodes`   | Lista episódios    |
| GET    | `/locations`  | Lista localizações |


Query Params

- limit → quantidade de registros (default: 10)
- name → filtro opcional por nome

Exemplo:
```/characters?limit=5&name=homer```

Testes com Swagger
O FastAPI gera automaticamente a documentação interativa:
Swagger UI

```http://127.0.0.1:8000/docs```

<img width="1454" height="751" alt="image" src="https://github.com/user-attachments/assets/0ae415e3-7253-4f07-9ee7-5bfae3f3672b" />


Nela é possível:

- Visualizar todas as rotas
- Informar parâmetros
- Executar requisições
- Ver respostas em tempo real

Integração Externa

Os dados são consumidos da API pública: https://thesimpsonsapi.com/api

A lógica de integração fica centralizada em services/simpsons_service.py, seguindo boas práticas de separação de responsabilidades.

Conclusão

Este projeto demonstra, de forma prática, como construir uma API REST moderna com FastAPI, aplicando conceitos fundamentais como organização por camadas, rotas bem definidas e integração com APIs externas.

Além de servir como material de estudo, o projeto é uma base sólida para aplicações reais, permitindo fácil evolução para novos recursos, autenticação e deploy em ambientes produtivos.


