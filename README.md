## Partidos API
Uma API usando python, sem framework. 

### Como usar?
Você pode usar com virtualenv or docker. 
 

#### Virtualenv

1 - Crie seu virtualenv e instale nele os pré-requisitos utilizando o comando a baixo

```bash
pip install -r requirements.txt 
```
2 - Na raiz do projeto crie um arquivo .env e adicione os dados abaixo 
```code
ALLOWED_HOSTS=*,127.0.0.1,
DATABASE_NAME=<name do seu banco>
DATABASE_USERNAME=<user do seu banconame>
DATABASE_PASSWORD=<your datababse password>
DATABASE_HOST=<host do seu banco>
DATABASE_PORT=<host do seu banco>
```
[P.S.: Necessário postgres instalado para rodar o projeto.]

3 - Após configurar o banco de dados, execute no virtualenv o seguinte comando para a criação da tabela: 

```bash
python migrate.py
```


4 - Após criar a tabela, utilize o comando abaixo para rodar a API: 

```bash
python api.py
```

#### Docker 

1 - Instalar/ter instalado docker e docker-compose


2 - Na raiz do projeto crie um arquivo .env e adicione os dados abaixo 
```code
ALLOWED_HOSTS=*,127.0.0.1,
DATABASE_NAME=localpostgres
DATABASE_USERNAME=localpostgres
DATABASE_PASSWORD=localpostgres
DATABASE_HOST=postgres
DATABASE_PORT=5432
```
3 - Utilize o comando abaixo para subir a API, o banco de dados e o frontend. 
```bash
[sudo] docker-compose up
```
[P.S.: Repositório do frontend: https://github.com/rafaeldblima/front-angular-eleicoes . Aplicação de frontend pode ser acessada em http://localhost]

##### URLS Partidos
Base = http://localhost:5000/api

| Name   | Method      | URL                    |
| ---    | ---         | ---                    |
| Home   | `GET`       | `/`             |
| Listar   | `GET`       | `/partidos`             |
| Criar | `POST`      | `/partidos`             |
| Buscar    | `GET`       | `/partidos/{id}`        |
| Atualizar | `PUT/PATCH` | `/partidos/{id}`        |
| Excluir | `DELETE`    | `/partidos/{id}`        |

