from .database import db

class ArticleTag(db.Model):
    __tablename__ = 'article_tags'
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)

    article = db.relationship('Article', backref='article_tags')
    tag = db.relationship('Tag', backref='article_tags')

    def __init__(self, article_id, tag_id):
        self.article_id = article_id
        self.tag_id = tag_id

    def serialize(self):
        return {
            'article_id': self.article_id,
            'tag_id': self.tag_id,
        }

    def __repr__(self):
        return f"ArticleTag {self.article_id}_{self.tag_id}"
