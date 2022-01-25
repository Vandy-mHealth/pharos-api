from uuid import UUID

import app.core.schemas as schemas
import app.db.crud as crud
from fastapi import APIRouter, Body, HTTPException, Query

user_router = APIRouter()


@user_router.get("/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100):
    return crud.get_users(skip, limit)


@user_router.post("/create", response_model=schemas.User)
def create_user(user: schemas.UserCreate):
    db_user = crud.get_user_by_email(email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400, detail=f"User already exists with name {db_user.email}"
        )

    return crud.create_user(user)


@user_router.put("/", response_model=schemas.User)
def update_user(user_id: UUID = Query(...), args: schemas.UserUpdate = Body(...)):
    db_user = crud.get_user_by_id(id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_user(user_id, args)


@user_router.post("/signin", response_model=schemas.User)
def signin(user: schemas.UserSignin):
    db_user = crud.get_user_by_email(email=user.email)

    if not db_user:
        raise HTTPException(status_code=400, detail="Email not found")

    if db_user.pin != user.pin:
        raise HTTPException(status_code=400, detail="Wrong pin number")

    return db_user
