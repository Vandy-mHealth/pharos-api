from uuid import UUID

import app.core.schemas as schemas
from app.db import Landmark, Network, Photo, User


def create_user(user: schemas.UserCreate):
    db_user = User.create(email=user.email, pin=user.pin, full_name=user.full_name)
    return db_user


def get_user_by_email(email: str):
    db_user = User.select().where(User.email == email).first()
    return db_user


def get_user_by_id(id: UUID):
    return User.select().where(User.id == id).first()


def get_user_landmarks(user_id: UUID, skip: int = 0, limit: int = 100):
    return list(
        Landmark.select()
        .join(User, on=(User.id == Landmark.owner_id))
        .join(Network, on=(Landmark.id == Network.landmark_id))
        .join(Photo, on=(Landmark.id == Photo.landmark_id))
        .where(User.id == user_id)
        .offset(skip)
        .limit(limit)
    )


def get_landmark_by_id(id: int):
    return Landmark.select().where(Landmark.id == id).first()


def create_user_landmark(
    user_id: UUID,
    landmark: schemas.LandmarkCreate,
    network: schemas.NetworkCreate,
    photo: schemas.PhotoCreate,
):
    landmark = Landmark.create(**landmark.dict(), owner_id=user_id)
    if network is not None:
        network = Network.create(
            **network.dict(), landmark_id=landmark.id, owner_id=user_id
        )
    if photo is not None:
        photo = Photo.create(**photo.dict(), landmark_id=landmark.id, owner_id=user_id)
    return landmark


def get_user_network_measurements(user_id: UUID, skip: int = 0, limit: int = 100):
    return list(
        Network.select()
        .join(User, on=(User.id == Network.owner_id))
        .where(User.id == user_id)
        .offset(skip)
        .limit(limit)
    )


def create_user_network_measurement(
    user_id: UUID, landmark_id: int, network: schemas.NetworkCreate
):
    return Network.create(**network.dict(), landmark_id=landmark_id, owner_id=user_id)


def get_user_photos(user_id: UUID, skip: int = 0, limit: int = 100):
    return list(
        Photo.select()
        .join(User, on=(User.id == Photo.owner_id))
        .where(User.id == user_id)
        .offset(skip)
        .limit(limit)
    )


def create_user_photo(user_id: UUID, landmark_id: int, photo: schemas.PhotoCreate):
    return Photo.create(**photo.dict(), landmark_id=landmark_id, owner_id=user_id)


# simple get queries
def get_users(skip: int = 0, limit: int = 100):
    return list(User.select().offset(skip).limit(limit))


def get_landmarks(skip: int = 0, limit: int = 100):
    return list(Landmark.select().offset(skip).limit(limit))


def get_network_measurements(skip: int = 0, limit: int = 100):
    return list(Network.select().offset(skip).limit(limit))


def get_photos(skip: int = 0, limit: int = 100):
    return list(Photo.select().offset(skip).limit(limit))
