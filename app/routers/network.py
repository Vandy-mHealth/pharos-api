from uuid import UUID

import app.core.schemas as schemas
import app.db.crud as crud
from fastapi import APIRouter, HTTPException, Query

network_router = APIRouter()


@network_router.get("/", response_model=list[schemas.Network])
def read_network_measurements(
    user_id: UUID = Query(None), skip: int = 0, limit: int = 100
):
    if user_id is None:
        return crud.get_network_measurements(skip, limit)
    else:
        return crud.get_user_network_measurements(user_id, skip, limit)


@network_router.post("/create", response_model=schemas.Network)
def create_network_measurements_for_user(
    user_id: UUID, landmark_id: int, network: schemas.NetworkCreate
):
    db_user = crud.get_user_by_id(id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_landmark = crud.get_landmark_by_id(id=landmark_id)
    if db_landmark is None:
        raise HTTPException(status_code=404, detail="Landmark not found")
    return crud.create_user_network_measurement(user_id, landmark_id, network)
