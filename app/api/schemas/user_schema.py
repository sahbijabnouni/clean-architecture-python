from marshmallow import Schema, fields, post_load
from app.core.entities.user import User

class UserSchema(Schema):
    id = fields.Str(required=True)
    firstName = fields.Str(required=True)
    lastName = fields.Str(required=True)
    email = fields.Str(required=True)

    @post_load
    def make_user_object(self, data, **kwargs):
        return User(data["id"], data["firstName"], data["lastName"], data["email"])