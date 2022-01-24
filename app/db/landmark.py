from datetime import datetime

from app.db.database import BasePeeweeModel
from peewee import (
    AutoField,
    CharField,
    DateTimeField,
    DoubleField,
    ForeignKeyField,
    IntegerField,
)

from .user import User


class Landmark(BasePeeweeModel):
    id = AutoField(primary_key=True, index=True)

    latitude = DoubleField()
    longitude = DoubleField()
    timestamp = DateTimeField(default=datetime.now())
    landmark_type = CharField()
    device_id = IntegerField()
    file_url = CharField()
    owner = ForeignKeyField(User, backref="landmarks")
