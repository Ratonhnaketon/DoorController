from flask_restful import Resource, reqparse, abort
from flask import request
from datetime import datetime
from db.models.logModel import LogModel
from db.schemas.logSchema import LogSchema

class LogResource(Resource):
	parser = reqparse.RequestParser()    
	parser.add_argument('doorStatus',
						type=str,
						required=True,
						help='doorStatus cant be blank.'
						)
	parser.add_argument('personName',
						type=str,
						required=False,
						)

	def get(self, item):
		json = ''
		try:
			log = LogModel.findByPersonName(item)
			print(log)
			if log:
				schema = LogSchema(exclude=['lists'])
				json = schema.dump(log).data
			else:
				return {'message':'Log of id {} dont found'.format(item)}, 404
		except Exception as e:
			print(e)
			return {'message','Error on request {}'.format(item)}, 500

		return json,200

	def post(self):
		try:
			data = LogResource.parser.parse_args()
			if not data:
				return {'message': 'Requisição sem JSON'}, 400

			log = LogModel(**data)
			log.add()
			schema = LogSchema(exclude=['lists'])
			json = schema.dump(log).data
			return json, 201

		except Exception as ex:
			print(ex)
			return {'message': 'error'}, 500

class LogsResource(Resource):
	def get(self):
		json = ''
		try:
			logs = LogModel.showAll()
			schema = LogSchema(many=True, exclude=['lists'])
			json = schema.dump(logs).data
		except Exception as e:
			print(e)
			return {'message': 'Error to retrieve list of logs'}, 500
		return json, 200