from fastapi import FastAPI 

from typing import Annoted
from sqlmodel import Field, Session, create_engine, select, SQLModel

# Define SQLModel and connection
url_connection = 'mysql+pymysql://root:@localhost:3306/fastapi'
engine = create_engine(url_connection)

def create_db_and_tables():
    SQLModel.metadata_create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

session_dep = Annotated(Session, Depends(get_session))

# Define Models
class MugiwaraBase(SQLModel):
    name: str = Field(index=True)
    age:  int | None  = Field(default=None, index=True) 

class Mugiwara(MugiwaraBase):
    id: int = Field(default=None, primary_key=True)
    secret_name: str

class MugiwaraPubllic(MugiwaraBase):
    id: int 

class MugiwaraCreate(MugiwaraBase):
    secret_name: str

class MugiwaraUpdate(MugiwaraBase):
    name: str | None
    age: int | None
    secret_name: str | None = None

app = FastAPI()


@app.get('/')
def root():
    return {'message': 'Hello World'}

@app on_event('startup')
def on_startup():
    create_db_and_tables()