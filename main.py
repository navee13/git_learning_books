from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field
from typing import Optional
from sqlmodel import Field, SQLModel, Session, create_engine, select
from fastapi.exceptions import HTTPException


app = FastAPI()
