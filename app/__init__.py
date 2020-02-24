from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from app.util import custom_json_output
from app.db import Database
from flask_jwt_extended import JWTManager
from app.config import Config 


app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
db = Database(app)
jwt = JWTManager(app)
api.representations.update({
    'application/json': custom_json_output
})
cors = CORS(app, resources={r"*": {"origins": "*"}})
from app.router import route