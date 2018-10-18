__author__ = " Rafael Lima"

import os

import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env(
)
envfile_path = os.path.join(BASE_DIR, '.env')
environ.Env.read_env(env_file=envfile_path)
# ALLow hosts
ALLOWED_HOSTS = env('ALLOWED_HOSTS')
'''
Database config
Se for utilizar com docker:
    "host": "postgres",
    "port": 5432
Se for utilizar com virtualenv:
    "host": "localhost",
    "port": 5432
'''

DATABASE = {
    "dbname": env('DATABASE_NAME'),
    "user": env('DATABASE_USERNAME'),
    "password": env('DATABASE_PASSWORD'),
    "host": env('DATABASE_HOST'),
    "port": env('DATABASE_PORT')
}

# end Database settings
