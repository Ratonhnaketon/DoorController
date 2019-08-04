from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from ServerController.db.models.loginModel import LoginModel

class LoginSchema(ModelSchema):
    class Meta:
        model = LoginModel