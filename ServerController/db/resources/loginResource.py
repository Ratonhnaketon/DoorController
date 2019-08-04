from flask_restful import Resource, reqparse, abort
from flask import request
from datetime import datetime
from ServerController.db.models.loginModel import LoginModel
from ServerController.db.schemas.loginSchema import LoginSchema

class LoginResource(Resource):
	parser = reqparse.RequestParser()    
	parser.add_argument('password',
						type=str,
						required=True,
						help='password cant be blank.'
						)
	parser.add_argument('isCreating',
						type=bool,
						required=False,
						)
	parser.add_argument('personName',
						type=str,
						required=False,
						)

	def post(self):
		try:
			data = LoginResource.parser.parse_args()
			if not data:
				return {'message': 'Request without JSON'}, 400

			user = LoginModel.findByPassword(data['password'])
			if data['isCreating']:
				if user:
					return { 'message': 'User already exists'}, 400 
				del data['isCreating']
				login = LoginModel(**data)
				login.add()
				schema = LoginSchema(exclude=['lists'])
				json = schema.dump(login).data
				return json, 201
			elif not user:
				return { 'message': 'Wrong password'}, 404 
			
			return { 'message': 'Success' }, 200

		except Exception as ex:
			print(ex)
			return {'message': 'error'}, 500
