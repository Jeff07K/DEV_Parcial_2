from typing import List
from fastapi import FastAPI, HTTPException, UploadFile, File
from sqlmodel import Session
from models.perritos import (perritos)
from models.trainer import TrainerBase, TrainerID
from db import  SessionDep, create_all_tables
from sqlmodel import select

app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
