from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from db.resources.logResource import LogsResource, LogResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

app.secret_key = b'\xc4]gW\x0f\x8d\xc8\x05ocG\xf1\xb1j,{'

CORS(app, resources={r"/*": {"origins": "*"}})  # O uso do cors

@app.before_first_request
def create_tables():
    from dao import db
    db.init_app(app)
    print("Creating tables")
    db.create_all()

class ServerController:
    def __init__(self):
        self.port = 5000
        self.debug = True
        self.api = Api(app)
        self.api.add_resource(LogsResource, '/logs')
        self.api.add_resource(LogResource, '/log', '/log/<int:item>')

    def init(port, debug):
        self.port = port
        self.debug = debug

    def run(self):
        from dao import db
        db.init_app(app)
        self.app.run(port=5000, debug=True)

svrController = ServerController()        
