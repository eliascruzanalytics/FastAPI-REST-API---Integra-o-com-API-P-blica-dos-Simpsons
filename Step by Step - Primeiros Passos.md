<img width="506" height="448" alt="image" src="https://github.com/user-attachments/assets/233eda80-90c8-4f8b-8706-368cfe5ccc50" />



## Clonar o Repositório

```git clone https://github.com/seu-usuario/seu-repositorio.git```

```cd seu-repositorio```


# Criar e Ativar o Ambiente Virtual (Opcional, mas recomendado)

```python -m venv venv```

```venv\Scripts\activate```

# Linux / Mac
```python3 -m venv venv```
```source venv/bin/activate```

# Instalar as Dependências

```pip install -r requirements.txt```

# Isso instalará:

- FastAPI
- Uvicorn
- Requests

# Entender o Arquivo Principal
O arquivo app.py é o ponto de entrada da aplicação, responsável por:

- Criar a instância do FastAPI
- Registrar todas as rotas da API

# Iniciar o Servidor Local
```uvicorn app:app --reload```

O parâmetro --reload reinicia o servidor automaticamente a cada alteração no código.

# Acessar a API
API rodando: http://127.0.0.1:8000  
Documentação interativa (Swagger): http://127.0.0.1:8000/docs

# Testar os Endpoints pelo Swagger
No Swagger você pode:

- Escolher um endpoint (/characters, /episodes, /locations)
- Informar parâmetros (limit, name)
- Clicar em Try it out
- Executar a requisição e ver a resposta

# Próximos passos:

- Criar novos endpoints
- Adicionar métodos POST, PUT e DELETE
- Implementar autenticação
- Preparar o projeto para deploy


# Resumo Final — Passos e Recomendações
Passos Principais

- Clonar o repositório
- Criar e ativar um ambiente virtual
- Instalar as dependências do projeto
- Iniciar o servidor com Uvicorn
- Acessar o Swagger para testar os endpoints
- Explorar e evoluir a API conforme necessidade

Recomendações

- Utilize sempre a documentação automática (/docs) para testes rápidos
- Mantenha a separação entre rotas e serviços
- Centralize integrações externas em uma camada específica
- Use tipagem para evitar erros e melhorar a legibilidade
- Evolua o projeto adicionando novos métodos HTTP e validações
- Use este projeto como base para estudos, aulas ou portfólio
