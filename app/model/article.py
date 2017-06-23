from .database import db
from timezone import localize

class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(45))
    body = db.Column(db.String(255))
    url = db.Column(db.String(255))
    thumbnail = db.Column(db.String(255))
    published_at = db.Column(db.DateTime(timezone=True))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    tags = db.relationship('Tag', secondary='article_tags')

    def __init__(self, title, body, url, thumbnail, published_at):
        self.title = title
        self.body = body
        self.url = url
        self.thumbnail = thumbnail
        self.published_at = published_at

    def serialize(self):
        published_at = localize(self.published_at)
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'url': self.url,
            'thumbnail': self.thumbnail,
            'published_at': f'{published_at}',
            'tags': [t.serialize() for t in self.tags]
        }

    def __repr__(self):
        return '<Article %r>' % self.title
