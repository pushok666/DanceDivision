from pydantic import BaseModel
from pydantic.fields import Field

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str

class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None

class AccountAuth(BaseModel):
    email: str = Field(..., description="User email")
    password: str = Field(..., min_length=5, max_length=24, description="User password")

class AccountBase(BaseModel):
    email: str


class AccountCreate(AccountBase):
    password: str
    username: str

    class Config:
        orm_mode = True

class Account(AccountBase):
    id: int
    name: str
    surname: str
    username: str
    age: int

    class Config:
        orm_mode = True


class OutAccount(AccountBase):
    id: int
    email: str


class InAccount(OutAccount):
    hashed_password: str

class TokenPayload(BaseModel):
    sub: str = None
    exp: int = None
