from uuid import UUID

import app.core.schemas as schemas
import app.db.crud as crud
from app.db import Photo
from fastapi import APIRouter, Query

photo_router = APIRouter()


@photo_router.get("/", response_model=list[schemas.Photo])
def read_photos(user_id: UUID = Query(None), skip: int = 0, limit: int = 100):
    if user_id is not None:
        return crud.get_user_photos(user_id, skip, limit)
    else:
        return crud.get_photos(skip, limit)


@photo_router.post("/create", response_model=schemas.Photo)
def create_photo_for_user(user_id: UUID, landmark_id: int, photo: schemas.PhotoCreate):
    return crud.create_user_photo(user_id, landmark_id, photo)
