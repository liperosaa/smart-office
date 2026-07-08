# Smart Office API

API REST desenvolvida com **FastAPI** para gerenciamento inteligente de escritórios, permitindo controlar usuários, salas, equipamentos, consumo energético e geração de relatórios.

O projeto foi desenvolvido com foco em boas práticas de arquitetura, organização do código, testes automatizados e documentação da API.

---

## Tecnologias

- Python 3.13
- FastAPI
- SQLAlchemy ORM
- Alembic
- SQLite
- Pydantic
- JWT Authentication (em desenvolvimento)
- Pytest
- Uvicorn
- Swagger/OpenAPI

---

# Arquitetura

```
backend/
│
├── app/
│   ├── auth/
│   ├── database/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   └── tests/
│
├── migrations/
├── alembic.ini
├── requirements.txt
└── .env
```

A API foi organizada utilizando arquitetura em camadas:

- Models
- Schemas
- Services
- Routes
- Authentication
- Database

---

# Funcionalidades Implementadas

## Usuários

- Cadastro
- Listagem
- Atualização
- Exclusão

---

## Salas

- Cadastro
- Listagem
- Atualização
- Exclusão

---

## Equipamentos

- Cadastro
- Listagem
- Atualização
- Exclusão

---

## Consumo de Energia

- Registro de consumo
- Histórico
- Consultas

---

## Dashboard

Indicadores gerais:

- Total de usuários
- Total de salas
- Total de equipamentos
- Consumo energético

---

## Relatórios

- Ranking de consumo
- Estatísticas
- Dados consolidados

---

## Banco de Dados

- SQLAlchemy ORM
- Alembic Migrations
- Versionamento do banco

---

## Testes Automatizados

Atualmente o projeto possui testes automatizados utilizando **Pytest**.

### Cobertura

```
81% de cobertura
```

Todos os testes estão passando.

---

# Autenticação

Foi iniciada a implementação de autenticação utilizando:

- JWT
- Password Hash (bcrypt)
- OAuth2 Password Flow

A integração completa será disponibilizada na próxima versão.

---

# Documentação

Após executar o projeto:

```
http://127.0.0.1:8000/docs
```

Swagger UI disponível.

---

# Executando

Clone o projeto

```bash
git clone https://github.com/liperosaa/smart-office.git
```

Crie o ambiente virtual

```bash
python -m venv .venv
```

Ative

Windows

```bash
.venv\Scripts\activate
```

Instale as dependências

```bash
pip install -r requirements.txt
```

Execute

```bash
uvicorn app.main:app --reload
```

---

# Roadmap

## v1.0

- CRUD Usuários
- CRUD Salas
- CRUD Equipamentos
- Gestão Energética
- Dashboard
- Relatórios
- Alembic
- Testes Automatizados

---

## v1.1

- Autenticação JWT
- Rotas Protegidas
- Controle de Permissões

---

## v1.2

- Refresh Token
- Logout
- Alteração de Senha

---

## v1.3

- PostgreSQL
- Docker
- Docker Compose

---

## v1.4

- Deploy
- CI/CD
- GitHub Actions

---

# Autor

**Felipe Padson Rosa da Silva**

Graduando em Ciência da Computação

LinkedIn:
https://www.linkedin.com/in/felipe-padson/

GitHub:
https://github.com/liperosaa