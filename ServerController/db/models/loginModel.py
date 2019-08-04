from ServerController.dao import db, Base
from datetime import datetime

class LoginModel(Base):
	__tablename__ = 'Users'
	id = db.Column(db.Integer, primary_key=True)
	password = db.Column(db.String(200), unique=True)
	personName = db.Column(db.String(200))

	def __init__(self, personName, password):
		self.personName = personName
		self.password = password 

	def add(self):
		db.session.add(self)
		db.session.commit()

	@classmethod
	def findByPassword(cls, _password):
		return cls.query.filter_by(password=_password).first()

