import uuid
from datetime import datetime

from app.db.database import BasePeeweeModel
from peewee import SQL, BigIntegerField, CharField, DateTimeField, UUIDField


class User(BasePeeweeModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    username = CharField(index=True, null=True)
    pin = BigIntegerField(null=True)
    last_login = DateTimeField(default=datetime.now())
