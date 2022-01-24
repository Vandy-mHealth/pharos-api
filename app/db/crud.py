import json
from datetime import date

import app.core.schemas as schemas
from app.db import Landmark, Network, Photo, User


def create_user(user: schemas.UserCreate):
    db_user = User.create(username=user.username, pin=user.pin)
    return db_user


def get_user_by_name(username: str):
    db_user = User.select().where(User.username == username).first()
    return db_user


def get_user_landmarks(user_id: str, skip: int = 0, limit: int = 100):
    return list(
        Landmark.select()
        .join(User, on=(User.id == Landmark.owner_id))
        .join(Network, on=(Landmark.id == Network.landmark_id))
        .join(Photo, on=(Landmark.id == Photo.landmark_id))
        .where(User.id == user_id)
        .offset(skip)
        .limit(limit)
    )


def create_user_landmark(
    user_id: str,
    landmark: schemas.LandmarkCreate,
    network: schemas.NetworkCreate,
    photo: schemas.PhotoCreate,
):
    landmark = Landmark.create(**landmark.dict(), owner_id=user_id)
    network = Network.create(**network.dict(), landmark_id=landmark.id)
    photo = Photo.create(**photo.dict(), landmark_id=landmark.id)
    return landmark


# simple get queries
def get_users(skip: int = 0, limit: int = 100):
    return list(User.select().offset(skip).limit(limit))


def get_landmarks(skip: int = 0, limit: int = 100):
    return list(
        Landmark.select()
        .join(User, on=(User.id == Landmark.owner_id))
        .join(Network, on=(Landmark.id == Network.landmark_id))
        .join(Photo, on=(Landmark.id == Photo.landmark_id))
        .offset(skip)
        .limit(limit)
    )


def get_network_measurements(skip: int = 0, limit: int = 100):
    return list(Network.select().offset(skip).limit(limit))


def get_photos(skip: int = 0, limit: int = 100):
    return list(Photo.select().offset(skip).limit(limit))
