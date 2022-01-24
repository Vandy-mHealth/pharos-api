from datetime import datetime
from typing import Any, List, Optional
from uuid import UUID

import peewee
from pydantic import BaseModel, EmailStr, Field
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
    owner_id: UUID

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class NetworkBase(BaseModel):
    ping_time: float
    frequency: float
    file_size: float
    file_location: str
    download_speed: float
    download_latency: float
    download_duration: float
    upload_speed: float
    upload_duration: float
    gps_latitude: float
    gps_longitude: float
    device_id: int


class NetworkCreate(NetworkBase):
    pass


class Network(NetworkBase):
    id: int
    timestamp: datetime
    landmark_id: int
    owner_id: UUID

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class LandmarkBase(BaseModel):
    latitude: float
    longitude: float
    landmark_type: str
    device_id: int
    file_url: str


class LandmarkCreate(LandmarkBase):
    pass


class Landmark(LandmarkBase):
    id: int
    timestamp: datetime
    owner_id: UUID
    network_measurements: List[Network] = []
    photos: List[Photo] = []

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class UserBase(BaseModel):
    email: EmailStr
    pin: int
    full_name: str


class UserSignin(BaseModel):
    email: EmailStr
    pin: int


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    pin: int = None
    full_name: str = None
    email: Optional[EmailStr] = None
    organization: Optional[str] = None
    address: Optional[str] = None


class User(UserBase):
    id: UUID
    created_at: datetime
    organization: Optional[str] = None
    address: Optional[str] = None

    landmarks: List[Landmark] = []
    photos: List[Photo] = []
    network_measurements: List[Network] = []

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
