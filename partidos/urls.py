import re

from partidos.views import *
from servers.status import *
from settings.response_messages import *

welcome = WelcomeView()
partidos = AllPartidos()
partido = GetPartido()
create_partido = CreatePartido()
update_partido = UpdatePartido()
delete_partido = DeletePartido()


def get_path(path, request_type, data=None):
    if request_type == 'GET':
        get_pk = re.findall("\d+", path)

        paths = [
            ('/', welcome.get()),
            ('/partidos', partidos.get()),
        ]
        if get_pk:
            pk = get_pk[0]
            paths = [
                ('/partidos/{}'.format(pk), partido.get(pk=pk)),
            ]

            if any(path in url for url in paths):
                if path == '/partidos/{}'.format(pk):

                    return paths[0][1].status_code, paths[0][1].data
                else:
                    return HTTP_404_NOT_FOUND, URL_NOT_FOUND

        if any(path in url for url in paths):

            if path == '/':
                return paths[0][1].status_code, paths[0][1].data

            elif path == '/partidos':

                return paths[1][1].status_code, paths[1][1].data

        else:
            return HTTP_404_NOT_FOUND, URL_NOT_FOUND

    elif request_type == 'POST':
        get_pk = re.findall("\d+", path)
        if get_pk:
            return HTTP_401_UNAUTHORIZED, UNAUTHORIZED

        paths = [
            ('/partidos', create_partido.post(data)),
        ]

        if any(path in url for url in paths):
            if path == '/partidos':
                return paths[0][1].status_code, paths[0][1].data

        else:
            return HTTP_404_NOT_FOUND, URL_NOT_FOUND

    elif request_type == 'PUT':
        get_pk = re.findall("\d+", path)

        if get_pk:
            pk = get_pk[0]
            paths = [
                ('/partidos/{}'.format(pk), update_partido.put(data=data, pk=pk)),
            ]

            if any(path in url for url in paths):
                if path == '/partidos/{}'.format(pk):
                    return paths[0][1].status_code, paths[0][1].data
                else:
                    return HTTP_404_NOT_FOUND, URL_NOT_FOUND

            return HTTP_404_NOT_FOUND, URL_NOT_FOUND

    elif request_type == 'PATCH':
        get_pk = re.findall("\d+", path)

        if get_pk:
            pk = get_pk[0]
            paths = [
                ('/partidos/{}'.format(pk), update_partido.patch(data=data, pk=pk)),
            ]

            if any(path in url for url in paths):
                if path == '/partidos/{}'.format(pk):
                    return paths[0][1].status_code, paths[0][1].data
                else:
                    return HTTP_404_NOT_FOUND, URL_NOT_FOUND

            return HTTP_404_NOT_FOUND, URL_NOT_FOUND

    elif request_type == 'DELETE':
        get_pk = re.findall("\d+", path)

        if get_pk:
            pk = get_pk[0]
            paths = [
                ('/partidos/{}'.format(pk), delete_partido.delete(pk=pk)),
            ]
            if path == '/partidos/{}'.format(pk):
                return paths[0][1].status_code, paths[0][1].data

            return HTTP_404_NOT_FOUND, URL_NOT_FOUND
        else:
            return HTTP_404_NOT_FOUND, URL_NOT_FOUND

    elif request_type == 'OPTIONS':
        get_pk = re.findall("\d+", path)

        paths = [
            ('/', welcome.get()),
            ('/partidos', partidos.get()),
        ]
        if get_pk:
            pk = get_pk[0]
            paths = [
                ('/partidos/{}'.format(pk), partido.get(pk=pk)),
            ]
            if any(path in url for url in paths):
                if path == '/partidos/{}'.format(pk):
                    return HTTP_200_OK, OPTIONS_PK_INFO, OPTIONS_PK_INFO_HEADERS

        if any(path in url for url in paths):

            if path == '/':
                return HTTP_200_OK, BASE_INFO, BASE_INFO_HEADERS

            elif path == '/partidos':

                return HTTP_200_OK, OPTIONS_INFO, OPTIONS_INFO_HEADERS

        else:
            return HTTP_404_NOT_FOUND, URL_NOT_FOUND, None
