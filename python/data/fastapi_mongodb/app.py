from fastapi import FastAPI 
from pymongo import mongo_client
import pydantic
from bson.objectid import ObjectId
import os.path
import json

pydantic.json.ENCODERS_BY_TYPE[ObjectId] = str

app = FastAPI()

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

HOSTNAME = get_secret("ATLAS_HOSTNAME")
USERNAME = get_secret("ATLAS_USERNAME")
PASSWORD = get_secret("ATLAS_PASSWORD")

client = mongo_client.MongoClient(f'mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}')
print('Connected to Mongodb….')


mydb = client['test']
mycol = mydb['testdb']

@app.get('/')
async def healthCheck():
    return "OK"

@app.get('/getmongo')
async def getMongo():
    return list(mycol.find().limit(10))

@app.get('/getuser')
async def getuser(id=None):
    if id is None:
        return 'id 를 입력하세요'
    result = mycol.find_one({'id':id})
    if result:
        return result
    else:
        return 'Not found'

@app.get('/useradd')
async def useradd(id=None, name=None):
    if (id and name) is None:
        return 'id, name 을 입력하세요'
    else:
        user = dict(id=id, name=name)
        mycol.insert_one(user)
        result = mycol.find_one({'id':id})
        return result

@app.get('/userupdate')
async def useradd(id=None, name=None):
    if (id and name) is None:
        return 'id, name 을 입력하세요'
    else:
        user = mycol.find_one({'id':id})
        if user:
            mycol.update_one({'id':id}, {"$set":{"name":name}})
            result = mycol.find_one({'id':id})
            return result
        else:
            return '해당하는 유저가 없어요.'

@app.get('/userremove')
async def useradd(id=None):
    if id is None:
        return 'id, name 을 입력하세요'
    else:
        user = mycol.find_one({'id':id})
        if user:
            mycol.delete_one({'id':id})
            return '삭제 되었습니다.'
        else:
            return '해당하는 유저가 없어요.'