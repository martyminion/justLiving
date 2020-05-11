from flask import render_template,redirect,request,abort,url_for
from . import main
from flask_login import login_required,current_user
from ..models import Blog,Comment,User
from .. import db,photos
from .forms import BlogForm,CommentForm,UpdateBio
import markdown2
from .. import mail
from flask_mail import Message
from ..requests import get_quotes
from sqlalchemy import desc
from markupsafe import Markup, escape

@main.route('/')
def index():
  '''
  this will define the view to go to the home page
  '''
  quote = get_quotes()

  title = "Homepage"

  return render_template('index.html',title  = title, quote = quote)

@main.route('/blogs')
def view_blogs():
  '''
  displays all the blogs
  '''
  blogs = Blog.query.order_by(desc(Blog.id)).all()
  
  title = "Just Living"
  return render_template('blogs.html',title = title, blogs = blogs)

@main.route('/<blogid>/blog')
def single_blog(blogid):
  '''
  displays a single blog
  '''
  comments = Comment.get_comments_by_blog_id(blogid)
  one_blog = Blog.get_blog_by_id(blogid)
  if one_blog is None:
    abort(404)

  format_blog = markdown2.markdown(one_blog.blog_body,extras=["code-friendly","fenced-code-blocks"])
  
  title = one_blog.title

  return render_template('singleblog.html',title = title, format_blog = format_blog,comments = comments,one_blog = one_blog)

@main.route('/new/blog',methods = ["GET","POST"])
@login_required
def add_blog():
  '''
  adds a new blog
  '''
  blog_form = BlogForm()

  if blog_form.validate_on_submit():
    new_blog = Blog(title = blog_form.title.data, category = blog_form.category.data, blog_body = blog_form.body.data)
    new_blog.save_blog()
    '''
    send bulk emails to all the readers
    '''
    readers = User.query.filter_by(role_id = 2).all()
    with mail.connect() as con:
      for reader in readers:
        subject = f"Check out {new_blog.title} on Just Living"
        email = Message(subject = subject, recipients = [reader.email])
        email.body = render_template('email/welcome_user.txt')
        email.html = render_template('email/welcome_user.html')

        con.send(email)
      
    return redirect(url_for('main.view_blogs'))
  title = "New Blog"
  return render_template('newblog.html',blogform = blog_form, title = title)

@main.route("/<blogid>/edit",methods = ['GET','POST'])
@login_required
def edit_blog(blogid):
  '''
  gives the writer ability to edit the blog
  '''
  form = BlogForm()
  blog = Blog.query.filter_by(id = blogid).first()
  form.title.data = blog.title
  form.category.data = blog.category
  form.body.data = blog.blog_body

  if request.method == 'POST':
    title = request.form['title']
    category = request.form['category']
    body = request.form['body']

    blog.title = title
    blog.category = category
    blog.blog_body = body
    db.session.commit()

    return redirect(url_for('main.single_blog',blogid = blog.id))
  title = "Edit Blog"

  return render_template('newblog.html',blogform = form, title = title) 

@main.route('/<blogid>/blog/delete',methods = ["GET","POST"])
@login_required
def delete_blog(blogid):
  '''
  deletes a blog
  '''
  delete_blog = Blog.query.filter_by(id = blogid).first()
  comments = Comment.query.filter_by(blog_id = blogid).all()
  #if there exists comments for that blog
  if comments:
    for comment in comments:
      db.session.delete(comment)

  db.session.delete(delete_blog)
  db.session.commit()

  return redirect(url_for('main.view_blogs'))


@main.route('/<readername>/<blogid>/new/comment',methods = ["GET","POST"])
@login_required
def add_comment(readername,blogid):
  reader = User.query.filter_by(username = readername).first()
  blog = Blog.query.filter_by(id = blogid).first()

  comment_form = CommentForm()
  if comment_form.validate_on_submit():
    comment = Comment(comment_body = comment_form.body.data,blog_id = blogid, user_id = reader.id )
    comment.save_comment()
    return redirect(url_for('main.single_blog',blogid = blogid))
  title = 'New Comment'
  return render_template("newcomment.html",comment_form = comment_form, title = title)

@main.route('/<commentid>/comment/delete')
@login_required
def delete_comment(commentid):
  '''
  deletes a comment
  '''
  delete_comment = Comment.query.filter_by(id = commentid).first()
  db.session.delete(delete_comment)
  db.session.commit()

  return redirect(request.referrer)

@main.route('/writer/profile/')
def profile():
  '''
  views the writer's profile
  '''
  writer = User.query.filter_by(role_id = 1).first()
  quote = get_quotes()

  title = "Profile"
  return render_template('profile.html',writer = writer,title = title, quote = quote)

@main.route("/<role>/update/pic/",methods = ['GET','POST'])
@login_required
def update_pic(role):
  '''
  updates the Writer's profile pic
  '''
  writer = User.query.filter_by(role_id = 1).first()
  if 'photo' in request.files:
    filename = photos.save(request.files['photo'])
    path = f'photos/{filename}'
    writer.prof_pic = path
    db.session.commit()
    return redirect(url_for('main.profile'))

@main.route("/<role>/update/bio",methods = ['GET','POST'])
@login_required
def update_bio(role):
  '''
  updates the writer's bio
  '''
  writer = User.query.filter_by(role_id = 1).first()

  form = UpdateBio()

  if form.validate_on_submit():
    writer.bio = form.bio.data
    db.session.commit()
    return redirect(url_for('main.profile'))
  return render_template('bio.html',form = form)

# @main.route('/send/mail')
# @login_required
# def send_emails():
#   '''
#   sends bulk emails to all the readers
#   '''
#   readers = User.query.filter_by(role_id = 2).all()
#   with mail.connect() as con:
#     for reader in readers:
#       subject = f"Welcome {reader.username} to Just Living"
#       email = Message(subject = subject, recipients = [reader.email])
#       email.body = render_template(template + 'email/welcome_user.txt',**kwargs)
#       email.html = render_template(template +'email/welcome_user.html',**kwargs)

#       con.send(email)
  
#   return redirect(request.referrer)