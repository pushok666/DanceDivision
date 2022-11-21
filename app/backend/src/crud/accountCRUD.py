import os
from sqlalchemy.orm import Session
from src.models import account
from src.schemas import accountSchema

def get_user(db: Session, account_id: int):
    return db.query(account.Accounts).filter(account.Accounts.id == account_id).first()

def create_user(db: Session, acc: accountSchema.AccountCreate):
    fake_hashed_password = acc.password + "notreallyhashed"
    db_acc = account.Accounts(email=acc.email, username=acc.username, password=fake_hashed_password, age=18)
    db.add(db_acc)
    db.commit()
    db.refresh(db_acc)
    return db_acc 

def get_user_by_email(db: Session, email:str):
    return db.query(account.Accounts).filter(account.Accounts.email == email).first()
