from flask import Blueprint, request,jsonify
from app.api.schemas.user_schema import UserSchema 
from marshmallow import Schema, fields, validate, ValidationError
from app.core.application.manager.user_manager import UserManager
from injector import inject
user_api = Blueprint('user_api', __name__)

@inject
@user_api.route("/api/user", methods=['POST'])
def add(user_manager:UserManager):
    try:
        user = UserSchema().load(request.json)
        user_manager.add(user);
    except ValidationError as err:
        return err.messages, 422
    return {}, 201

@inject
@user_api.route("/api/user/<id>", methods=['GET'])
def find(id:str,user_manager:UserManager):
    user=user_manager.find(id)
    return UserSchema().dump(user), 200