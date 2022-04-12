from flask import Flask 
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

from google.appengine.ext import webapp

view_routes = [

]

app = Flask(__name__, static_folder = "static")
