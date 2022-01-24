from datetime import datetime

from app.db.database import BasePeeweeModel
from peewee import (
    SQL,
    AutoField,
    CharField,
    DateTimeField,
    DoubleField,
    ForeignKeyField,
    IntegerField,
)

from .landmark import Landmark
from .user import User


class Network(BasePeeweeModel):
    id = AutoField(primary_key=True, index=True)

    ping_time = DoubleField()
    frequency = DoubleField()
    file_size = DoubleField()
    file_location = CharField()
    download_speed = DoubleField()
    download_latency = DoubleField()
    download_duration = DoubleField()
    upload_speed = DoubleField()
    upload_duration = DoubleField()
    timestamp = DateTimeField(default=datetime.now())
    gps_longitude = DoubleField()
    gps_latitude = DoubleField()
    device_id = IntegerField()

    landmark = ForeignKeyField(Landmark, backref="network_measurements")
    owner = ForeignKeyField(User, backref="network_measurements")
