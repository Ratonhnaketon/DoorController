    
from dao import db,Base
from datetime import datetime

class LogModel(Base):
	__tablename__ = 'Logs'
	id = db.Column(db.Integer, primary_key=True)
	doorStatus = db.Column(db.String(200))
	personName = db.Column(db.String(200))
	dateTime = db.Column(db.DateTime)

	def __init__(self, personName, doorStatus):
		self.personName = personName
		self.doorStatus = doorStatus 
		self.dateTime = datetime.now()

	def add(self):
		db.session.add(self)
		db.session.commit()

	@classmethod
	def findByPersonName(cls, _personName):
		return cls.query.filter_by(personName=_personName).all()

	@classmethod
	def showAll(cls):
		return cls.query.all()
