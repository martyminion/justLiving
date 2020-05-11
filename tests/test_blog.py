import unittest
from app.models import User,Comment,Blog,Roles
from app import db


class BlogTest(unittest.TestCase):
  '''
  Test class for the blog model
  '''

  def setUp(self):
    '''
    runs at the beginning of t