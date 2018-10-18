from psycopg2 import connect

from settings.settings import DATABASE

db_connection = connect(**DATABASE)

db = db_connection.cursor()
