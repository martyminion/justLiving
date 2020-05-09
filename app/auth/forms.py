from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,PasswordField,SelectField,SubmitField,BooleanField
from wtforms.validators import email,Required,Email,EqualTo
from ..models import Writer,Reader
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
  '''
  form to be filled by a new reader
  '''
  email = StringField("Please Enter you email", validators=[Required(),email()])
  username = StringField("Enter a cool Username", validators=[Required()])
  password = PasswordField("Enter a password you can remember",validators=[Required(),EqualTo('password_confirm',message="You already Forgot the Password")])
  password_confirm = PasswordField('Can you remember the password', validators=[Required()])
  submit = SubmitField('Sign Up')

  #custom validators

  def validate_email(self,data_field):
    '''
    checks if there exists a similar email
    '''
    if Reader.query.filter_by(email = data_field.data).first():
      raise ValidationError('You are already on our reader list')

  def validate_username(self,data_field):
    '''
    checks if there exists a similar username
    '''
    if Reader.query.filter_by(username = data_field.data).first():
      raise ValidationError("This username is soo cool it's taken")

class LoginForm(FlaskForm):
  '''
  form to be filled during log in
  '''
  role = SelectField("Sign in as: ",choices=[("reader","reader"),("writer","writer")],validators=[Required()])
  email = StringField("Please enter your email",validators=[Required()])
  password = PasswordField("Let's see if you remember your password",validators=[Required()])
  remember = BooleanField("Remember me")
  submit = SubmitField("Always nice to see you")
