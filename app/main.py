from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://news:secret@db/news'
db = SQLAlchemy(app)


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

    def __repr__(self):
        return '<Article %r>' % self.title


@app.route('/')
def index():
    articles = Article.query.all()
    # article = Article.query.filter_by(id=1).all()
    # for article in articles:
    #     app.logger.debug(article.title)

    return "Hello world!!"