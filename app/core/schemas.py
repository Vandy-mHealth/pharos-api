from datetime import datetime
from typing import Any, List, Optional
from uuid import UUID

import peewee
from pydantic import BaseModel
from pydantic.utils import GetterDict


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res


class PhotoBase(BaseModel):
    url: str


class PhotoCreate(PhotoBase):
    pass


class Photo(PhotoBase):
    id: int
    uploaded_at: datetime
    landmark_id: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class NetworkBase(BaseModel):
    ping_time: float
    frequency: float
    file_size: float
    file_url: float
    download_speed: float
    download_latency: float
    download_duration: float
    upload_speed: float
    upload_duration: float
    network_strength: float


class NetworkCreate(NetworkBase):
    pass


class Network(NetworkBase):
    id: int
    timestamp: datetime
    landmark_id: int

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class LandmarkBase(BaseModel):
    lat: float
    lon: float
    landmark_type: str
    gps_strength: str


class LandmarkCreate(LandmarkBase):
    pass


class Landmark(LandmarkBase):
    id: int
    owner_id: UUID
    network_measurements: List[Network] = []
    photos: List[Photo] = []

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    pin: int


class User(UserBase):
    id: UUID
    pin: int
    last_login: datetime
    landmarks: List[Landmark] = []

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
