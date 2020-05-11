import unittest
from app.models import User
from app import db


class UserTest(unittest.TestCase):
  '''
  Test class for the User class
  '''
  def setUp(self):
    '''
    Set up method that will run before all the test
    '''
    self.new_user = User(email = 'diana@gmail.com',username = 'shiks',
    password = 'banana',prof_pic = 'path/to/image', bio = "I love flowers",role_id = 1 )

    db.session.add(self.new_user)
    db.session.commit()

  def tearDown():
    '''
    runs after every test to clear the data
    '''
    User.query.delete()
    db.session.commit()

  def test_password_setter(self):
    self.assertTrue(self.new_user.pass_secure is not None)

  def test_verify_password(self):
    self.assertTrue(self.new_user.verify_password(password))

  def test_variable_instantiation(self):
    '''
    confirm that the variables are instantiated correctly
    '''
    self.assertEqual(self.new_user.email,"diana@gmail.com")
    self.assertEqual(self.new_user.username,"shiks")
    self.assertEqual(self.new_user.prof_pic,"path/to/image")
    self.assertEqual(self.new_user.bio,"I love flowers")
    self.assertEqual(self.new_user.role_id, 1)

  def test_no_acces_password(self):
    '''
    check if an error will be thrown if password is accessed
    '''
    with self.assertRaises(AttributeError):
      self.new_user.password
  



