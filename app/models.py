from datetime import datetime
from hashlib import md5
from time import time
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from app import app, db, login

followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    forumspost = db.relationship('ForumsPost', backref='postauthor', lazy='dynamic')
    forumspostscontect = db.relationship('ForumsPostContect', backref='postcontectauthor', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


# ---------------------------Forums---------------------------

class ForumsTopic(db.Model):
    __tablename__ = 'forums_topic'
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(80), index=True)
    type = db.Column(db.String(50))
    description = db.Column(db.String(150))
    url = db.Column(db.String(140), index=True)


class ForumsPost(db.Model):
    __tablename__ = 'forums_post'
    id = db.Column(db.Integer, primary_key=True, index=True)
    subject = db.Column(db.String(180), index=True)
    url = db.Column(db.String(140), index=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('forums_topic.id'))
    writer_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class ForumsPostContect(db.Model):
    __tablename__ = 'forums_post_contect'
    id = db.Column(db.Integer, primary_key=True, index=True)
    contect = db.Column(db.String(300))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('forums_post.id'))
    writer_id = db.Column(db.Integer, db.ForeignKey('user.id'))






# ---------------------------NavBar---------------------------

class Mainbar(db.Model):
    __tablename__ = 'Main_bar'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    Name = db.Column(db.String(80), nullable=False)
    url = db.Column(db.String(140), nullable=False)


# -------------------------SubBar----------------------------
class MySQLBar(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    Name = db.Column(db.String(80), nullable=False)
    url = db.Column(db.String(140), nullable=False)
    MainID = db.Column(db.Integer, db.ForeignKey('Main_bar.id'), nullable=False)


class DZBar(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    Name = db.Column(db.String(80), nullable=False)
    url = db.Column(db.String(140), nullable=False)
    MainID = db.Column(db.Integer, db.ForeignKey('Main_bar.id'), nullable=False)






# ---------------------------FLOVEMOVIE---------------------------


class index_product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producttitle = db.Column(db.String(50))
    url = db.Column(db.String(140))


class Product_Enterprise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    url = db.Column(db.String(140))
    indexID = db.Column(db.Integer, db.ForeignKey(index_product.id))


class Product_SqlClound(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    url = db.Column(db.String(140))
    indexID = db.Column(db.Integer, db.ForeignKey(index_product.id))


class Product_Cluster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    url = db.Column(db.String(140))
    indexID = db.Column(db.Integer, db.ForeignKey(index_product.id))


class ProductForOME(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    url = db.Column(db.String(140))
    indexID = db.Column(db.Integer, db.ForeignKey(index_product.id))


class NewestMovie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    url = db.Column(db.String(140))
    urlForimage = db.Column(db.String(140))
    indexID = db.Column(db.Integer, db.ForeignKey(index_product.id))


class CustomerLogo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    urlForimage = db.Column(db.String(140))
    url = db.Column(db.String(140))
    indexID = db.Column(db.Integer, db.ForeignKey(index_product.id))


class CinemaHongKong(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    url = db.Column(db.String(140))
    indexID = db.Column(db.Integer, db.ForeignKey(index_product.id))


class CinemaKowloon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    url = db.Column(db.String(140))
    indexID = db.Column(db.Integer, db.ForeignKey(index_product.id))


class CinemaNewTerritories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    url = db.Column(db.String(140))
    indexID = db.Column(db.Integer, db.ForeignKey(index_product.id))


class InsertMovie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    url = db.Column(db.String(140))
    urlForimage = db.Column(db.String(140))
    description = db.Column(db.String(1000))
    indexID = db.Column(db.Integer, db.ForeignKey(index_product.id))

class Partner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(50))
    url = db.Column(db.String(140))
    urlForimage = db.Column(db.String(140))
    indexID = db.Column(db.Integer, db.ForeignKey(index_product.id))

class BestMoviePicture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Moviename = db.Column(db.String(50))
    urlForimage = db.Column(db.String(140))
    indexID = db.Column(db.Integer, db.ForeignKey(index_product.id))

