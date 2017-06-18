from flask import Blueprint, jsonify, request, current_app
from model.article import Article
from model.tag import Tag
from model.article_tag import ArticleTag
from model.database import db
from validator.schemas import add_schema
from validator.validator import validate_schema

api = Blueprint("api", __name__, url_prefix="/v1")


DEFAULT_ARTICLE_LIMIT  = 5
DEFAULT_TAG_LIMIT      = 50
DEFAULT_ARTICLE_OFFSET = 0


'''
GET tag_articles
'''
@api.route('/articles/tag/<string:tag_name>')
def show_tag_articles(tag_name):

    limit  = _get_article_limit(request.args.get('limit'))
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

    limit  = _get_article_limit(request.args.get('limit'))
    offset = _get_offset(request.args.get('offset'))

    articles = Article.query \
        .order_by(Article.published_at.desc(), Article.id.desc())\
        .offset(offset)\
        .limit(limit)
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
Get tags
'''
@api.route('/tags')
def show_tags():
    limit  = _get_tag_limit(request.args.get('limit'))
    offset = _get_offset(request.args.get('offset'))

    tags = Tag.query \
        .order_by(Tag.id) \
        .offset(offset)\
        .limit(limit)

    tag_count = Article.query.count()
    next_offset = min(limit + offset, tag_count)
    is_next = next_offset != tag_count

    return jsonify(
        tags=[a.serialize() for a in tags],
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

def _get_article_limit(l):
    return int(l) if l is not None else DEFAULT_ARTICLE_LIMIT

def _get_tag_limit(l):
    return int(l) if l is not None else DEFAULT_TAG_LIMIT

def _get_offset(o):
    return int(o) if o is not None else DEFAULT_ARTICLE_OFFSET
