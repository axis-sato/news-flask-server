from .database import db

class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(45))
    body = db.Column(db.String(255))
    url = db.Column(db.String(255))
    thumbnail = db.Column(db.String(255))

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
            'thumbnail': self.thumbnail
        }

    def __repr__(self):
        return '<Article %r>' % self.title


