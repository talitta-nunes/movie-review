# Movie-Review

Aplicação para gerenciar usuários, filmes e reviews.

# Projeto Django REST API

Este projeto é uma aplicação Django que oferece uma API RESTful para gerenciamento de entidades e relacionamentos.

## Funcionalidades Principais

- Customização de usuário com base no AbstractUser.
- Registro de modelos no Django Admin.
- Diagrama de Entidade e Relacionamento.
- Serializers convencionais.
- Validação customizada.
- Sobrescrita de métodos de serializers.
- Proteção de rotas via autenticação auth token e custom permissions do Django Rest Framework.
- ModelSerializer para a Review.
- Campos de escolha para atributos de model.
- Paginação com APIView.

## Instalação e Configuração

1. Clone o repositório: `git clone https://github.com/talitta-nunes/movie-review.git`
2. Navegue até o diretório do projeto: `cd movie-review`
3. Crie um ambiente virtual: `python -m venv venv`
4. Ative o ambiente virtual: 
   - No Windows: `venv\Scripts\activate`
   - No macOS e Linux: `source venv/bin/activate`
5. Instale as dependências: `pip install -r requirements.txt`
6. Execute as migrações: `python manage.py migrate`
7. Inicie o servidor: `python manage.py runserver`


### Endpoints da aplicação:
| Método | Endpoint | Objetivo | Autorização Token |
|---|---|---|---|
| `POST` | `/api/users/register/` |Criação de um crítico de filmes ou de um usuário comum | `Não` |
| `POST` | `/api/login/` |Autenticar um usuário e retornar um token de acesso | `Não` |
| `GET` | `/api/users/` |Listar todos os usuários | `Sim` |
| `GET` | `/api/users/<int:user_id>/` | Filtrar um usuário | `Sim` |
| `GET` | `/api/movies/` |Listar todos os filmes | `Não` |
| `POST` | `/api/movies/` |Criação de um filme | `Sim` |
| `GET` | `/api/movies/<int:movie_id>/` |Filtrar um filme | `Não` |
| `DELETE` | `/api/movies/<int:movie_id>/` |Deletar um filme | `Sim` |
| `PATCH` | `/api/movies/<int:movie_id>/` |Atualizar um filme | `Sim` |
| `POST` | `/api/movies/<int:movie_id>/reviews/` |Criação de uma nova review para o filme | `Sim` |
| `GET` | `/api/movies/<int:movie_id>/reviews/` |Listagem das reviews do filme em questão | `Não` |
| `GET` | `/api/movies/<int:movie_id>/reviews/<int:review_id>/` |Filtragem da review do filme em questão | `Não` |
| `DELETE` | `/api/movies/<int:movie_id>/reviews/<int:review_id>/` |Deleção da review do filme em questão | `Sim` |

## Diagrama

![image](https://github.com/talitta-nunes/movie-review/assets/70520439/f0449c2c-ad49-47a1-96f5-647e496bb7d4)



