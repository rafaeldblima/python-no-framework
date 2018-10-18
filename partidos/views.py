from db.querys import add_partido, update_partido, delete_partido, get_all_partidos, get_partido_by_id
from partidos.validation import validate_required_fields, validate_patch
from servers import status
from servers.response import Response
from settings.response_messages import DATA_NOT_FOUND


class WelcomeView:

    def get(self):
        data = 'Api para partidos.'
        return Response(data=data, status=status.HTTP_200_OK)


class AllPartidos:

    def get(self):
        data = get_all_partidos()
        return Response(data=data, status=status.HTTP_200_OK)


class GetPartido:

    def get(self, pk=None):
        partido = get_partido_by_id(pk)
        if partido:
            return Response(data=partido, status=status.HTTP_200_OK)
        else:
            return Response(data=DATA_NOT_FOUND, status=status.HTTP_200_OK)


partido_get = GetPartido()


class CreatePartido:

    def post(self, data):
        message, status_code = validate_required_fields(data)
        if status_code is status.HTTP_202_ACCEPTED:
            message, status_code = add_partido(data=data)
        return Response(data=message, status=status_code)


class UpdatePartido:

    def put(self, data, pk=None):
        message, status_code = validate_required_fields(data)
        if status_code is status.HTTP_202_ACCEPTED:
            data['id'] = pk
            partido = get_partido_by_id(pk)
            if partido:
                message, status_code = update_partido(data)
                return Response(data=message, status=status_code)
            else:
                return Response(data=DATA_NOT_FOUND, status=status.HTTP_200_OK)

        return Response(data=message, status=status_code)

    def patch(self, data, pk=None):
        data['id'] = pk
        message, status_code = validate_patch(data)
        if status_code is status.HTTP_202_ACCEPTED:
            partido = get_partido_by_id(pk)
            if partido:
                if data['nome']:
                    partido['nome'] = data['nome']
                if data['sigla']:
                    partido['sigla'] = data['sigla']
                if data['numero']:
                    partido['numero'] = data['numero']
                if data['fundo']:
                    partido['fundo'] = data['fundo']
                message, status_code = update_partido(partido)
                return Response(data=message, status=status_code)
            else:
                return Response(data=DATA_NOT_FOUND, status=status.HTTP_200_OK)
        return Response(data=message, status=status_code)


class DeletePartido:

    def delete(self, pk=None):
        data = {"id": pk}
        partido = get_partido_by_id(pk)
        if partido:
            message, status_code = delete_partido(data)
            return Response(data=message, status=status_code)
        else:
            return Response(data=DATA_NOT_FOUND, status=status.HTTP_200_OK)
