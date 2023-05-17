import requests, json 
import pandas as pd 
from datetime import datetime , timedelta
import os.path
from fastapi import FastAPI

# BASE_DIR = os.path.dirname((os.path.relpath("./")))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
secret_file = os.path.join(BASE_DIR, './pythonDBProcess/secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg
    
app = FastAPI()

@app.get('/')
async def healthCheck():
    return "{'code':'OK'}"
@app.get('/hello')
async def hello():
    return "{'greeting':'Hello World'}"

@app.get('/getdata')
async def getData():
    url = 'https://apis.data.go.kr/1352000/ODMS_COVID_02/callCovid02Api'

    today = (datetime.today() - timedelta(1)).strftime("%Y%m%d")
    print(today)

    params = '?serviceKey=' + get_secret("data_apiKey")
    params += "&pageNo=1"
    params += "&numOfRows=500"
    params += "&apiType=JSON"
    params += "&status_dt="+str(today)

    url += params
    print(url)

    response = requests.get(url)
    print(response)
    print('-'*50)

    contents = response.text
    print(type(contents))
    print(contents)
    print('-'*50)

    dictionary = json.loads(contents)
    print(type(dictionary))
    print(dictionary)
    print('-'*50)

    items = dictionary['items'][0]
    print(type(items))
    print(items)
    print('-'*50)

    item = ['gPntCnt','hPntCnt','accExamCnt','statusDt']
    validItems = dict({(k, v) for (k, v) in items.items() if k in item})
    # validItems = dict({(k, v) for (k, v) in items.fromkeys(item).items()})
    print(items.fromkeys(item))
    print(type(validItems))
    print(validItems)
    # print('-'*50)

    validItem = {}
    for _ in item:
        validItem[_] = items[_]
    print(validItem)

    return validItem
