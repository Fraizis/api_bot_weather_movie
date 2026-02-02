from peewee import (
    CharField,
    Model,
    SqliteDatabase,
    IntegerField,
    DateTimeField
)

db = SqliteDatabase('database.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    user_id = IntegerField()
    user_message = CharField()
    date = DateTimeField()


User.create_table()
