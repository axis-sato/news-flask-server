from flask import Flask
from model.database import setup_db
from logger import setup_logger
from controller.article import api

app = Flask(__name__)
setup_db(app)
setup_logger(app)

app.register_blueprint(api)
