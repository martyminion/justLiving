from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from sqlalchemy import desc


class User(db.Model,UserMixin):
  '''
  describes the attributes we will require from a writer
  '''
  __tablename__="users"
  id = db.Column(db.Integer,primary_key = True)
  email = db.Column(db.String(255),unique = True, index = True)
  username = db.Column(db.String(255),index = True)
  pass_secure = db.Column(db.String())
  prof_pic = db.Column(db.String())
  bio = db.Column(db.String())
  role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
  comments = db.relationship('Comment',backref = 'feedback', lazy = 'dynamic')

  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')

  @password.setter
  def password(self, password):
    self.pass_secure = generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.pass_secure,password)

  @login_manager.user_loader
  def load_user(user_id):
    '''
    call back function that returns the reader when a unique identifier is passed
    '''
    return User.query.get(int(user_id))

class Roles(db.Model):
  '''
  defines the 2 roles of either reader or writer
  '''
  __tablename__ = "roles"
  id = db.Column(db.Integer,primary_key = True)
  name = db.Column(db.String(255))
  users = db.relationship('User',backref = 'role', lazy = 'dynamic')
  

class Blog(db.Model):
  '''
  defines the characteristics of a blog
  '''
  __tablename__ = "blogs"
  id = db.Column(db.Integer,primary_key = True)
  title = db.Column(db.String(255))
  category = db.Column(db.String())
  blog_body = db.Column(db.String())

  comments = db.relationship('Comment',backref = 'comment', lazy = 'dynamic')

  def save_blog(self):
    '''
    adds new blog to database
    '''
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_blog_by_id(cls,blog_id):
    '''
    gets the blogs by id
    '''
    blog = Blog.query.filter_by(id = blog_id).first()

    return blog


class Comment(db.Model):
  '''
  defines the attributes of a comment
  '''
  __tablename__ = "comments"
  id = db.Column(db.Integer,primary_key = True)
  comment_body = db.Column(db.String())
  blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  def save_comment(self):
    '''
    adds new comment to database
    '''
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_comments_by_blog_id(cls,blog_id):
    '''
    gets the comments for a particular blog
    '''
    comments = Comment.query.filter_by(blog_id = blog_id).all()

    return comments

class Quote:
  '''
  defines the quote attributes
  '''

  def __init__(self,id,author,quote):
    self.id = id
    self.author = author
    self.quote = quote
