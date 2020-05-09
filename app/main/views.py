from flask import render_template,redirect,request,abort
from . import main
from flask_login import login_required
from ..models import Blog,Comment,Reader
from .. import db
from .forms import BlogForm,CommentForm

@main.route('/')
def index():
  '''
  this will define the view to go to the home page
  '''
  
  title = "Homepage"

  return render_template('index.html',title  = title)

@main.route('/blogs')
def view_blogs():
  '''
  displays all the blogs
  '''
  blogs = Blog.query.all()
  title = "Just Living"
  render_template('blogs.html',title = title, blogs = blogs)

@main.route('/<blogid>/blog')
def single_blog(blogid):
  '''
  displays a single blog
  '''
  comments = Comment.query.filter_by(blog_id = blogid).all()
  one_blog = Blog.query.filter_by(id = blogid).first()
  title = one_blog.title

  render_template('singleblog.html',title = title, one_blog = one_blog,comments = comments)

@main.route('/new/blog')
@login_required
def add_blog():
  '''
  adds a new blog
  '''
  blog_form = BlogForm()

  if blog_form.validate_on_submit():
    new_blog = Blog(title = blog_form.title.data, category = blog_form.category.data, blog_body = blog_form.body.data)
    new_blog.save_blog()
  ##### return redirect('blogs.html')
  title = "New Blog"
  return render_template('newblog.html',blogform = blog_form, title = title)

@main.route('/<readername>/<blogid>/new/comment')
@login_required
def add_comment(readername,blogid):
  reader = Reader.query.filter_by(username = readername).first()
  blog = Blog.query.filter_by(id = blogid).first()

  comment_form = CommentForm()
  if comment_form.validate_on_submit():
    comment = Comment(comment_body = comment_form.body.data,blog_id = blogid, reader_id = reader.id )
    comment.save_comment()
  #####return redirect('')
  title = 'New Comment'
  return render_template("newcomment.html",comment_form = comment_form, title = title)