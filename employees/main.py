from fastapi import FastAPI, status, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from sqlmodel import SQLModel, create_engine
import models
import schemas

engine = create_engine('sqlite:///./employees.db', connect_args={"check_same_thread": False})

def get_session():
    with Session(engine) as session:
        yield session

def create_table():
    SQLModel.metadata.create_all(engine)


SessionConn = Annotated[Session, Depends(get_session)]


app = FastAPI()

@app.get("/", status_code=status.HTTP_200_OK)
def get_user(response: schemas.User, db: SessionConn):
    print('hello')
    users = db.query(models.Employee).all()
    print(users)
    return {"users": users}


@app.post('/user/', status_code=status.HTTP_201_CREATED)
def user(request: models.Employee, session: SessionConn):
    session.add(request)
    session.commit()
    session.refresh(request)
    return request
