from typing import List

import app.core.schemas as schemas
import app.db.crud as crud
from app.db import User
from fastapi import APIRouter, HTTPException, Query
from playhouse.shortcuts import model_to_dict

user_router = APIRouter()


@user_router.post("/create", response_model=schemas.User)
def create_user(user: schemas.UserCreate):
    db_user = crud.get_user_by_name(username=user.username)
    if db_user:
        raise HTTPException(
            status_code=400, detail=f"User already exists with name {db_user.username}"
        )

    return crud.create_user(user)


@user_router.get("/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100):
    return crud.get_users(skip, limit)
