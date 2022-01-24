import uuid
from datetime import datetime

from app.db.database import BasePeeweeModel
from peewee import SQL, BigIntegerField, CharField, DateTimeField, UUIDField


class User(BasePeeweeModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    email = CharField()
    pin = BigIntegerField()
    full_name = CharField()
    created_at = DateTimeField(default=datetime.now)
    organization = CharField(null=True)
    address = CharField(null=True)
