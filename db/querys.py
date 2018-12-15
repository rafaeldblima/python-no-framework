import datetime

from db.database_connection import db_connection, db
from settings.response_messages import *


def get_all_partidos():
    db.execute(
        "SELECT id, nome, sigla, fundo, numero, created_at "
        "FROM partido ORDER BY id ASC")

    partidos = []
    for item in db.fetchall():
        data = dict()
        data['id'] = item[0]
        data['nome'] = item[1]
        data['sigla'] = item[2]
        if item[3]:
            data['fundo'] = float(item[3])
        data['numero'] = item[4]
        data['created_at'] = item[5].strftime('%Y-%m-%dT%H:%M:%S')
        partidos.append(data)
    return partidos


def get_partido_by_id(partido_id):
    db.execute(
        "SELECT id, nome, sigla, fundo, numero, created_at "
        f"FROM partido where id = {partido_id}")

    partidos = []
    for item in db.fetchall():
        data = dict()
        data['id'] = item[0]
        data['nome'] = item[1]
        data['sigla'] = item[2]
        if item[3]:
            data['fundo'] = float(item[3])
        data['numero'] = item[4]
        data['created_at'] = item[5].strftime('%Y-%m-%dT%H:%M:%S')
        partidos.append(data)
    return partidos[0] if len(partidos) > 0 else None


def add_partido(data):
    try:
        db.execute("INSERT INTO partido (nome, sigla, fundo, numero, created_at) VALUES (%s, %s, %s, %s, %s)",
                   (data['nome'], data['sigla'], data['fundo'], data['numero'], datetime.datetime.now()))
        db_connection.commit()

        status_code = 201
        return PARTIDO_CREATED, status_code
    except Exception as e:
        db_connection.rollback()
        return {'errors': e.args}, 400


def update_partido(data):
    try:
        db.execute("UPDATE partido SET nome=%s, sigla=%s, fundo=%s, numero=%s WHERE id=%s",
                   (data['nome'], data['sigla'], data['fundo'], data['numero'], data['id']))
        db_connection.commit()

        status_code = 200
        return PARTIDO_UPDATED, status_code
    except Exception as e:
        db_connection.rollback()
        return {'errors': e.args}, 400


def delete_partido(data):
    try:
        db.execute("DELETE FROM partido where id=%s" % data['id'])
        db_connection.commit()
        status_code = 200
        return PARTIDO_DELETED, status_code
    except Exception as e:
        db_connection.rollback()
        return {'errors': e.args}, 400
