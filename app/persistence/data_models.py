from peewee import *
import datetime


db = SqliteDatabase('/Users/sahbijabnouni/Documents/Projects/clean-architecture-python/_database/user.db')

class BaseModel(Model):
    class Meta:
        database = db

class UserTable(BaseModel):
    id = CharField(unique=True)
    firstName = TextField()
    lastName = TextField()
    email = TextField()
