from flask import Flask, jsonify
from model.article import Article
from model.database import setup_db
from logger import setup_logger

app = Flask(__name__)
setup_db(app)
setup_logger(app)


@app.route('/')
def index():
    articles = Article.query.all()
    app.logger.debug(articles)
    app.logger.info(articles)
    app.logger.warn(articles)
    app.logger.error(articles)

    return jsonify(articles=[a.serialize() for a in articles])
