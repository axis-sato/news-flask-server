from flask import Flask, jsonify
from model.article import Article
from model.database import db

app = Flask(__name__)
db.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://news:secret@db/news'


@app.route('/')
def index():
    articles = Article.query.all()
    app.logger.error(articles)

    return jsonify(articles=[a.serialize() for a in articles])
