from flask import Flask

service = Flask(__name__)
from service import views
