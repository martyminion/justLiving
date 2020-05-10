from flask import render_template,redirect,request,url_for,flash
from . import auth
from .forms import RegistrationForm,LoginForm
from ..models import Reader,Writer
from flask_login import login_user,logout_user,login_required
from .. import db
@auth.route('/login',methods = ['GET','POST'])
def login():
  '''
  defines the view for a writer and Reader login

  '''
  login_form = LoginForm()

  if login_form.validate_on_submit():
    if login_form.role.data == "writer":
      reader = Reader.query.filter_by(email = login_form.email.data).first()
      if reader is not None:
        flash('You are not a writer! Please sign in as a Reader')

      writer = Writer.query.filter_by(email = login_form.email.data).first()
      if writer is not None and writer.verify_password(login_form.password.data):
        login_user(writer,login_form.remember.data)
        return redirect(request.args.get('next') or url_for('main.index'))
      
    elif login_form.role.data == "reader":
      writer = Writer.query.filter_by(email = login_form.email.data).first()
      if writer is not None:
        flash('Please Sign in as a Writer')
      reader = Reader.query.filter_by(email = login_form.email.data).first()
      if reader is not None and reader.verify_password(login_form.password.data):
        login_user(reader,login_form.remember.data)
        return redirect(request.args.get('next') or url_for('main.index'))

    flash('Looks like you are new here or you forgot your credentials')

  title = "Login"

  return render_template('auth/login.html',login_form = login_form, title = title)
      

@auth.route('/register',methods = ['GET','POST'])
def register():
  form = RegistrationForm()

  if form.validate_on_submit():
    reader = Reader(email = form.email.data, username = form.username.data, password = form.password.data, role_id = 2)
    db.session.add(reader)
    db.session.commit()

    return redirect(url_for('auth.login'))
    title = "New Reader"

  return render_template('auth/register.html',registration_form = form)

@auth.route("/logout")
@login_required
def logout():
  logout_user()
  return redirect(url_for('main.index'))