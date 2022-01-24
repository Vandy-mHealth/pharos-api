import datetime
from datetime import datetime

from app.db.database import BasePeeweeModel
from peewee import SQL, AutoField, CharField, DateTimeField, ForeignKeyField

from .landmark import Landmark


class Photo(BasePeeweeModel):
    id = AutoField(primary_key=True, index=True)
    url = CharField()
    uploaded_at = DateTimeField(default=datetime.now())
    landmark = ForeignKeyField(Landmark, backref="photos")
