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
    posts = db.relationship('Post', backref='author', lazy='dynamic')
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

    def followed_posts(self):
        followed = Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
            followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())

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


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Product(db.Model):
    title_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))


class Topic(db.Model):
    title_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))


class ProductMysqlServer(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(140))
    name = db.Column(db.String(80))
    title_id = db.Column(db.Integer, db.ForeignKey('product.title_id'))


class ProductXDevAPI(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(140))
    name = db.Column(db.String(80))
    title_id = db.Column(db.Integer, db.ForeignKey('product.title_id'))


class ProductMySQLNDBCluster(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(140))
    name = db.Column(db.String(80))
    title_id = db.Column(db.Integer, db.ForeignKey('product.title_id'))


class TopicGeneral(db.Model):
    doc_id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(140))
    name = db.Column(db.String(80))
    title_id = db.Column(db.Integer, db.ForeignKey('topic.title_id'))


class TopicAdministrator_Guides(db.Model):
    doc_id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(140))
    name = db.Column(db.String(80))
    title_id = db.Column(db.Integer, db.ForeignKey('topic.title_id'))


class TopicHA_Scalability(db.Model):
    doc_id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(140))
    name = db.Column(db.String(80))
    title_id = db.Column(db.Integer, db.ForeignKey('topic.title_id'))


class Mainbar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80))
    url = db.Column(db.String(140))


class Title(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80))
    url = db.Column(db.String(140))
    MainID = db.Column(db.Integer, db.ForeignKey(Mainbar.id))


class EnterpriseDownload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    MainID = db.Column(db.Integer, db.ForeignKey(Mainbar.id))


class ClusterDownload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    MainID = db.Column(db.Integer, db.ForeignKey(Mainbar.id))


class MySQLCommunity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    version = db.Column(db.String(100))
    description = db.Column(db.String(200))
    com_link = db.Column(db.String(200))
    MainID = db.Column(db.Integer, db.ForeignKey(Mainbar.id))


class Windows(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    win_link = db.Column(db.String(200))
    MainID = db.Column(db.Integer, db.ForeignKey(Mainbar.id))


# ---------------------------Download---------------------------


class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


# class Downloads(db.Model):
#    Dow_id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(50))
#
#
# class Documentation(db.Model):
#    Doc_id = db.Column(db.Integer, primary_key=True)
#    name = db.column(db.String(50))
#    pr_id = db.Column(db.Integer, db.ForeignKey("product.title_id"))
#    top_id = db.Column(db.Integer, db.ForeignKey("topic.title_id"))
#
# class Developer_zone(db.Model):
#    Dev_id=db.Column(db.Integer,primary_key=True)
#    name=db.column(db.String(50))

# ---------------------------MySql---------------------------



class index_product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producttitle = db.Column(db.String(50))
    url = db.Column(db.String(140))


class Product_Enterprise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    url = db.Column(db.String(140))
    indexID= db.Column(db.Integer, db.ForeignKey(index_product.id))


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

class CustomerLogo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    urlForimage = db.Column(db.String(140))
    url = db.Column(db.String(140))
    indexID = db.Column(db.Integer, db.ForeignKey(index_product.id))







