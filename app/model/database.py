from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def setup_db(app: Flask):
    db.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://news:secret@db/news'
