import app.core.schemas as schemas
import app.db.crud as crud
from fastapi import APIRouter, HTTPException, Query

user_router = APIRouter()


@user_router.get("/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100):
    return crud.get_users(skip, limit)


@user_router.post("/create", response_model=schemas.User)
def create_user(user: schemas.UserCreate):
    db_user = crud.get_user_by_email(email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400, detail=f"User already exists with name {db_user.username}"
        )

    return crud.create_user(user)


@user_router.post("/signin", response_model=schemas.User)
def signin(user: schemas.UserSignin):
    db_user = crud.get_user_by_email(email=user.email)

    if not db_user:
        raise HTTPException(status_code=400, detail="Email not found")

    if db_user.pin != user.pin:
        raise HTTPException(status_code=400, detail="Wrong pin number")

    return db_user
