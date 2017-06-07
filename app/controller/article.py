from flask import Blueprint, jsonify, request, current_app
from model.article import Article

api = Blueprint("api", __name__, url_prefix="/v1")


@api.route('/articles')
def show_articles():
    l = request.args.get('limit')
    limit = int(l) if l is not None else 5

    o= request.args.get('offset')
    offset = int(o) if o is not None else 0

    articles = Article.query.offset(offset).limit(limit)
    # current_app.logger.debug(articles)

    articles_count = Article.query.count()
    next_offset = min(limit + offset, articles_count)
    is_next = next_offset != articles_count

    return jsonify(
        articles=[a.serialize() for a in articles],
        nextOffset=next_offset,
        isNext=is_next,
        limit=limit
    )
