from fastapi import FastAPI

from pik_vision.schemas import UserPublic, UserSchema

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Hello World!'}


@app.post('/users/', response_model=UserPublic, tags=['Users'])
def create_user(user: UserSchema):
    return user
