from flask import Flask, jsonify, request
from model.article import Article
from model.database import setup_db
from logger import setup_logger

app = Flask(__name__)
setup_db(app)
setup_logger(app)


@app.route('/')
def index():
    limit = int(request.args.get('limit'))
    if limit is None:
        limit = 5
    offset = int(request.args.get('offset'))
    if offset is None:
        offset = 0

    articles = Article.query.offset(offset).limit(limit)
    app.logger.debug(articles)

    articles_count = Article.query.count()
    next_offset = min(limit + offset, articles_count)
    is_next = next_offset != articles_count

    return jsonify(
        articles=[a.serialize() for a in articles],
        nextOffset=next_offset,
        isNext=is_next,
        limit=limit
    )
