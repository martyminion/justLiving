from . import db

class Writer(db.Model):
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
  role_id = db.Column(db.Integer)



class Reader(db.Model):
  '''
  describes the attributes of a user
  '''
  __tablename__ = "readers"
  id = db.Column(db.Integer,primary_key = True)
  email = db.Column(db.String(255),unique = True, index = True)
  username = db.Column(db.String(255),index = True)
  pass_secure = db.Column(db.String())
  role_id = db.Column(db.Integer)

  comments = db.relationship('Comment',backref = 'comment', lazy = 'dynamic')

class Roles(db.Model):
  '''
  defines the 2 roles of either reader or writer
  '''
  __tablename__ = "roles"
  id = db.Column(db.Integer,primary_key = True)
  name = db.Column(db.String(255))

  

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
  reader_id = db.Column(db.Integer, db.ForeignKey('readers.id'))

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
    comments = Comment.query.filter_by(id = blog_id).all()

    return comments