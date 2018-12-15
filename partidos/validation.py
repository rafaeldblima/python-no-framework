from servers import status


def validate_patch(data):
    stat = status.HTTP_202_ACCEPTED
    errors = []
    if 'nome' in data and len(str(data['nome']).strip()) < 1 or not data['nome']:
        errors.append('Informe o nome do partido.')
        stat = status.HTTP_400_BAD_REQUEST
    if 'sigla' in data and len(str(data['sigla']).strip()) < 1 or not data['sigla']:
        errors.append('Informe a sigla do partido.')
        stat = status.HTTP_400_BAD_REQUEST
    if 'numero' not in data or not data['numero']:
        errors.append('Informe o numero do partido.')
        stat = status.HTTP_400_BAD_REQUEST
    elif 'numero' in data and not isinstance(data['numero'], int):
        errors.append('Formato inválido para o campo número.')
        stat = status.HTTP_400_BAD_REQUEST
    if 'fundo' in data and data['fundo'] and not isinstance(data['fundo'], (int, float)):
        errors.append('Formato inválido para o campo fundo.')
        stat = status.HTTP_400_BAD_REQUEST
    return {'errors': errors}, stat


def validate_required_fields(data):
    stat = status.HTTP_202_ACCEPTED
    errors = []
    if 'nome' not in data or not data['nome']:
        errors.append('Informe o nome do partido.')
        stat = status.HTTP_400_BAD_REQUEST
    if 'sigla' not in data or not data['sigla']:
        errors.append('Informe a sigla do partido.')
        stat = status.HTTP_400_BAD_REQUEST
    if 'numero' not in data or not data['numero']:
        errors.append('Informe o numero do partido.')
        stat = status.HTTP_400_BAD_REQUEST
    elif 'numero' in data and not isinstance(data['numero'], int):
        errors.append('Formato inválido para o campo número.')
        stat = status.HTTP_400_BAD_REQUEST
    if 'fundo' in data and data['fundo'] and not isinstance(data['fundo'], (int, float)):
        errors.append('Formato inválido para o campo fundo.')
        stat = status.HTTP_400_BAD_REQUEST
    return {'errors': errors}, stat
