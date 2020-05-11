from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import email,Required,Email,EqualTo
from ..models import Blog,Comment
from wtforms import ValidationError

class BlogForm(FlaskForm):
  '''
  defines the fields to be filled when writing a blog
  '''
  title = StringField("Title",validators=[Required()])
  category = StringField("Category",validators=[Required()])
  body = TextAreaField("Body")
  submit = SubmitField("Add")

class CommentForm(FlaskForm):
  '''
  defines the fields to be filled for a comment
  '''
  body = TextAreaField('Always be Kind')
  SubmitField = SubmitField('comment')

class UpdateBio(FlaskForm):
  '''
  defines the fields for a bio update
  '''
  bio = TextAreaField("How do you feel today")
  submit = SubmitField("Update Bio")
