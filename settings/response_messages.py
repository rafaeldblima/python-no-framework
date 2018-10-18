URL_NOT_FOUND = {"message": "URL não encontrada."}
DATA_NOT_FOUND = {"message": "Partido não encontrado."}
INVALID_REQUEST = {"message": "Método não suportado."}

UNAUTHORIZED = {"message": "Não autorizado."}

PARTIDO_CREATED = {"message": "Partido criado."}
PARTIDO_UPDATED = {"message": "Partido atualizado."}
PARTIDO_DELETED = {"message": "Partido excluído."}

BASE_INFO = {
    "GET": {
        "descricao": "Exibe a informação inicial da API."
    },
    "OPTIONS": {
        "descricao": "Retorna os endpoints que a url suporta."
    }
}

BASE_INFO_HEADERS = 'GET, OPTIONS'

OPTIONS_INFO = {
    "GET": {
        "descricao": "Exibe todos os partidos cadastrados no banco."
    },
    "POST": {
        "descricao": "Salva um partido no banco de dados.",
        "exemplo": {
            "nome": "NOVO",
            "sigla": "NOVO",
            "numero": 30,
            "fundo": 1000
        }
    },
    "OPTIONS": {
        "descricao": "Retorna os endpoints que a url suporta."
    }
}

OPTIONS_INFO_HEADERS = 'GET, POST, OPTIONS'

OPTIONS_PK_INFO = {
    "GET": {
        "descricao": "Busca um partido pelo seu id, id enviado pela url."
    },
    "PUT": {
        "descricao": "Atualiza todos os dados de um partido pelo seu id, id enviado pela url.",
        "exemplo": {
            "nome": "Partido dos Trabalhadores",
            "sigla": "PT",
            "numero": 13,
            "fundo": 1000
        }
    },
    "PATCH": {
        "descricao": "Atualiza os dados de um partido pelo seu id, id enviado pela url.",
        "exemplo": {
            "nome": "Partido Trabalhadores"
        }
    },
    "DELETE": {
        "descricao": "Exclui um partido pelo seu id, id enviado pela url."
    },
    "OPTIONS": {
        "descricao": "Retorna os endpoints que a url suporta."
    }
}

OPTIONS_PK_INFO_HEADERS = 'GET, PUT, PATCH, DELETE, OPTIONS'
