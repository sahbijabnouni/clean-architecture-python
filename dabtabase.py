from app.persistence.data_models import db
from app.persistence.data_models import UserTable
db.connect()
db.create_tables([UserTable])