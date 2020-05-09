from flask import render_template,redirect,request,abort
from . import main
from flask_login import login_required
from ..models import Blog,Comment
from .. import db
from .forms import BlogForm,CommentForm

@main.route('/')
def index():
  '''
  this will define the view to go to the home page
  '''
  
  title = "Homepage"

  return render_template('index.html',title  = title)

@main.route('/new/blog')
def add_blog():
  '''
  adds a new blog
  '''
  blog_form = BlogForm()

  if blog_form.validate_on_submit():
    new_blog = Blog(title = blog_form.title.data, category = blog_form.category.data, blog_body = blog_form.body.data)
    new_blog.save_blog()
    return redirect('blogs.html')
  title = "New Blog"
  return render_template('newblog.html',blogform = blog_form, title = title)

