from flask import Blueprint, jsonify, request, current_app
from model.article import Article

api = Blueprint("api", __name__, url_prefix="/v1")

@api.route('/articles')
def show_articles():
    limit = int(request.args.get('limit'))
    if limit is None:
        limit = 5
    offset = int(request.args.get('offset'))
    if offset is None:
        offset = 0

    current_app.logger.debug(f"offset: {offset}")
    current_app.logger.debug(f"limit: {limit}")

    articles = Article.query.offset(offset).limit(limit)
    current_app.logger.debug(articles)

    articles_count = Article.query.count()
    next_offset = min(limit + offset, articles_count)
    is_next = next_offset != articles_count

    return jsonify(
        articles=[a.serialize() for a in articles],
        nextOffset=next_offset,
        isNext=is_next,
        limit=limit
    )
