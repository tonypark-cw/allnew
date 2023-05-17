from fastapi import FastAPI
from pydantic.main import BaseModel

app = FastAPI()

class HelloWorldRequest(BaseModel):
    name:str
    age: int

@app.get(path='/')
async def hello():
    return 'hello world'


@app.get(path='/helloq/query')
async def helloq_query(name:str):
    return '안녕 '+ name + ' 야?'

@app.get(path='/hello/{name}')
async def hello_param(name:str):
    return '안녕, 너는  '+ name + ' 구나'


@app.post(path='/hello/post')
async def hello_query(reqeust:HelloWorldRequest):
    return '안녕 {}아 너는 {}살 이구나.'.format(reqeust.name, reqeust.age)