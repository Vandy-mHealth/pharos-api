from datetime import datetime
from tokenize import StringPrefix

from app.db.database import BasePeeweeModel
from peewee import AutoField, CharField, DateTimeField, DoubleField, ForeignKeyField

from .user import User


class Landmark(BasePeeweeModel):
    id = AutoField(primary_key=True, index=True)

    lat = DoubleField()
    lon = DoubleField()
    timestamp = DateTimeField(default=datetime.now())
    landmark_type = CharField()
    gps_strength = CharField()

    owner = ForeignKeyField(User, backref="landmarks")
