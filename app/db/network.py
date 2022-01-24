from datetime import datetime

from app.db.database import BasePeeweeModel
from peewee import (
    SQL,
    AutoField,
    CharField,
    DateTimeField,
    DoubleField,
    ForeignKeyField,
)

from .landmark import Landmark


class Network(BasePeeweeModel):
    id = AutoField(primary_key=True, index=True)

    ping_time = DoubleField()
    frequency = DoubleField()
    file_size = DoubleField()
    file_url = CharField()
    download_speed = DoubleField()
    download_latency = DoubleField()
    download_duration = DoubleField()
    upload_speed = DoubleField()
    upload_duration = DoubleField()
    network_strength = CharField()
    timestamp = DateTimeField(default=datetime.now())

    landmark = ForeignKeyField(Landmark, backref="network_measurements")
