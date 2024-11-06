from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from typing import Optional
from sqlmodel import Field, SQLModel, Session, create_engine, select
from fastapi.exceptions import HTTPException


class BookBase(SQLModel):
    title: str = Field(index=True)
    author: str
    isbn: str = Field(min_length=4, max_length=5, default="0011")
    description: Optional[str]


class Book(BookBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


app = FastAPI()
