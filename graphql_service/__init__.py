# Imports
import pymysql
from flask import Flask
from flask_restplus import Api
from flask_cors import CORS

pymysql.install_as_MySQLdb()

# app initialization
app = Flask(__name__)
CORS(app)

api = Api(app)