from .database import db

class Test(db.Model):
    __tablename__ = 'test'
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'), primary_key=True)
    name = db.Column(db.String(10))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Test {self.name}>'
