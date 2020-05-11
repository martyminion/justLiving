import unittest
from app.models import User,Comment,Blog,Roles,Quote
from app import db


class BlogTest(unittest.TestCase):
  '''
  Test class for the blog model
  '''

  def setUp(self):
    '''
    runs at the beginning of eah test to set up th attributes
    '''
    self.new_user = User(email = 'diana@gmail.com',username = 'shiks',
    password = 'banana',prof_pic = 'path/to/image', bio = "I love flowers",role_id = 1 )

    self.new_blog = Blog(title = "Monday", category = "Tuesday", blog_body = "Wednesday" )

    self.new_comment = Comment(comment_body = "Friday", blog_id = 3, user_id = 1)

    self.new_quote = Quote(id = 2, author = "James", quote = "Play Nice")

    db.session.add(self.new_user)
    db.session.add(self.new_blog)
    db.session.add(self.new_comment)
    db.session.commit()

  def tearDown(self):
    '''
    runs after every test to clear the data
    '''
    Comment.query.delete()
    Blog.query.delete()
    User.query.delete()
    db.session.commit()


  def test_blog_instance(self):
    '''
    check for proper instantiation of blog
    '''
    self.assertEqual(self.new_blog.title,"Monday")
    self.assertEqual(self.new_blog.category,"Tuesday")
    self.assertEqual(self.new_blog.blog_body,"Wednesday")

  def test_comment_instance(self):
    '''
    check for proper instantiation of comment
    '''
    self.assertEqual(self.new_comment.comment_body,"Friday")
    self.assertEqual(self.new_comment.blog_id,1)
    self.assertEqual(self.new_comment.user_id,1)

  def test_quote_instance(self):
    '''
    check for proper instantiation of Quote
    '''
    self.assertEqual(self.new_quote.id,2)
    self.assertEqual(self.new_quote.author,"James")
    self.assertEqual(self.new_quote.quote,"Play Nice")

    