from fastapi import FastAPI
from pydantic import BaseModel
import redis
import json

app = FastAPI()

rd = redis.Redis(host='localhost', port=6382, db=0)

class Estimation(BaseModel):
    assetType: str
    value: int
    timestamp: str

@app.get('/')
def read_root():
    return {'message': 'Hello World!'}

@app.post('/simulation')
def simulation(data: Estimation):
    cache = rd.get(f'assets:{data.assetType}')
    if cache:
        data = json.loads(cache)
        return data
    else:
        rd.set(f'assets:{data.assetType}', json.dumps(data.dict()))
        return data.dict()


