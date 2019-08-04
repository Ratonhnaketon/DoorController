from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from ServerController.db.models.logModel import LogModel

class LogSchema(ModelSchema):
    class Meta:
        model = LogModel