from fastapi import FastAPI
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
import os.path
import json


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
secret_file = os.path.join(BASE_DIR, '../secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg

HOSTNAME = get_secret("MYSQL_HOSTNAME")
port = get_secret("MYSQL_Port")
USERNAME = get_secret("MYSQL_USERNAME")
PASSWORD = get_secret("MYSQL_PASSWORD")
dbname = get_secret("MYSQL_DBname")

DB_URL = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{port}/{dbname}'

class db_conn:
    def __init__(self):
        self.engine = create_engine(DB_URL, pool_recycle=500)

    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def connection(self):
        conn = self.engine.connection()
        return conn


