import os
from fastapi import FastAPI, Depends, HTTPException, Request, Response
from sqlalchemy.orm import Session


from src.crud import accountCRUD
from src.models import account
from src.schemas import accountSchema

from src.database.database import SessionLocal, engine

from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse

from reprlib import db
from src.schemas.accountSchema import InAccount, OutAccount, TokenSchema, AccountAuth

account.Base.metadata.create_all(bind=engine)
#print(os.environ["POSTGRES_DB"])
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Interial server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

def get_db(request: Request):
    return request.state.db

# @app.get('/')
# def root():
#     return "Hello"

@app.get('/user/{user_id}', response_model=accountSchema.Account)
def read_account(user_id: int, db: Session = Depends(get_db)):
    db_account = accountCRUD.get_user(db, user_id=user_id)
    if db_account is None:
        raise HTTPException(status_code=404, detail="Account is not found")
    return db_account


@app.post('/users', response_model=accountSchema.AccountCreate)
def add_user(user: accountSchema.AccountCreate, db: Session = Depends(get_db)):
    db_user = accountCRUD.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return accountCRUD.create_user(db=db, acc=user)

@app.get('/', response_class=RedirectResponse, include_in_schema=False)
async def docs():
    return RedirectResponse(url='/docs')