from uuid import UUID

import app.core.schemas as schemas
import app.db.crud as crud
from fastapi import APIRouter, Body, HTTPException, Query

photo_router = APIRouter()


@photo_router.get("/", response_model=list[schemas.Photo])
def read_photos(user_id: UUID = Query(None), skip: int = 0, limit: int = 100):
    if user_id is not None:
        return crud.get_user_photos(user_id, skip, limit)
    else:
        return crud.get_photos(skip, limit)


@photo_router.post("/create", response_model=schemas.Photo)
def create_photo_for_user(
    user_id: UUID = Query(...),
    landmark_id: int = Query(...),
    photo: schemas.PhotoCreate = Body(...),
):
    db_user = crud.get_user_by_id(id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_landmark = crud.get_landmark_by_id(id=landmark_id)
    if db_landmark is None:
        raise HTTPException(status_code=404, detail="Landmark not found")
    return crud.create_user_photo(user_id, landmark_id, photo)
