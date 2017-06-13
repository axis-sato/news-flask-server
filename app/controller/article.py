from flask import Blueprint, jsonify, request, current_app
from model.article import Article
from model.tag import Tag
from model.article_tag import ArticleTag
from model.database import db
from validator.schemas import add_schema
from validator.validator import validate_schema

api = Blueprint("api", __name__, url_prefix="/v1")


DEFAULT_ARTICLE_LIMIT  = 5
DEFAULT_ARTICLE_OFFSET = 0


'''
GET tag_articles
'''
@api.route('/articles/tag/<string:tag_name>')
def show_tag_articles(tag_name):

    limit  = _get_limit(request.args.get('limit'))
    offset = _get_offset(request.args.get('offset'))
    current_app.logger.debug(tag_name)

    query = db.session.query(Article) \
        .join(ArticleTag, Tag) \
        .filter(Tag.name == tag_name) \

    articles = query.limit(limit).offset(offset)
    articles_count = query.count()

    next_offset = min(limit + offset, articles_count)
    is_next = next_offset != articles_count

    return jsonify(
        articles=[a.serialize() for a in articles],
        nextOffset=next_offset,
        isNext=is_next,
        limit=limit,
        offset=offset
    )


'''
GET articles
'''
@api.route('/articles')
def show_articles():

    limit  = _get_limit(request.args.get('limit'))
    offset = _get_offset(request.args.get('offset'))

    articles = Article.query.offset(offset).limit(limit)
    # current_app.logger.debug(articles)

    articles_count = Article.query.count()
    next_offset = min(limit + offset, articles_count)
    is_next = next_offset != articles_count

    return jsonify(
        articles=[a.serialize() for a in articles],
        nextOffset=next_offset,
        isNext=is_next,
        limit=limit,
        offset=offset
    )


'''
Post add
'''
@api.route('/add', methods=['POST'])
@validate_schema(add_schema)
def add():

    current_app.logger.debug(request.json)
    article_id = request.json['article_id']
    tag_names  = request.json['tag_names']

    article = Article.query\
        .filter(Article.id == article_id)\
        .first()

    current_app.logger.debug(article)

    # Pocketにpostする


    return jsonify(
        article.serialize()
    )


'''
Methods
'''

def _get_limit(l):
    return int(l) if l is not None else DEFAULT_ARTICLE_LIMIT

def _get_offset(o):
    return int(o) if o is not None else DEFAULT_ARTICLE_OFFSET
