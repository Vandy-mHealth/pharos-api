from uuid import UUID

import app.core.schemas as schemas
import app.db.crud as crud
from app.db import User
from fastapi import APIRouter, Query

landmark_router = APIRouter()


@landmark_router.get(
    "/",
    response_model=list[schemas.Landmark],
    description="query all landmarks or by user id",
)
def read_landmarks_for_user(
    user_id: UUID = Query(None, description="user id of whom uploads the landmark"),
    skip: int = 0,
    limit: int = 100,
):
    if user_id:
        return crud.get_user_landmarks(user_id=user_id, skip=skip, limit=limit)
    else:
        return crud.get_landmarks(skip=skip, limit=limit)


@landmark_router.post("/create", response_model=schemas.Landmark)
def create_landmark_for_user(
    user_id: UUID,
    landmark: schemas.LandmarkCreate,
    network: schemas.NetworkCreate,
    photo: schemas.PhotoCreate,
):
    return crud.create_user_landmark(user_id, landmark, network, photo)
