from .database import db

class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(45))
    body = db.Column(db.String(255))
    url = db.Column(db.String(255))
    thumbnail = db.Column(db.String(255))
    tags = db.relationship('Tag', secondary='article_tags')

    def __init__(self, title, body, url, thumbnail):
        self.title = title
        self.body = body
        self.url = url
        self.thumbnail = thumbnail

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'url': self.url,
            'thumbnail': self.thumbnail,
            # 'tags': self.tags
        }

    def __repr__(self):
        return '<Article %r>' % self.title

class ArticleTag(db.Model):
    __tablename__ = 'article_tags'
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))

    # def __init__(self):
    #     pass

    def serialize(self):
        return {
            'article_id': self.article_id,
            'tag_id': self.tag_id,
        }

    def __repr__(self):
        return f"ArticleTag {self.article_id}_{self.tag_id}"

class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    # article = db.relationship('Article', secondaly='article_tags')

    def __init__(self, name):
        self.name = name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def __repr__(self):
        return f"<Tag {self.name}>"
