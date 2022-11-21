from sqlalchemy import Boolean, Column, ForeignKey, INTEGER, VARCHAR, String
from sqlalchemy.orm import relationship

from src.database.database import Base

class Accounts(Base):
    __tablename__ = "accounts"

    id = Column("id", INTEGER, primary_key=True, index=True, autoincrement=True)
    email = Column("email", VARCHAR(255), unique=True, nullable=False)
    password = Column("password", VARCHAR(255))
    name = Column("name",VARCHAR(255))
    surname = Column("surname", VARCHAR(255))
    username = Column("username", VARCHAR(255), unique=True, nullable=False)
    age = Column("age", INTEGER)
    photo = Column("photo", String)

