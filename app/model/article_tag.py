from .database import db

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
