from flask import render_template,redirect,request,url_for
from . import auth
from .forms import RegistrationForm
from ..models import Writer,Reader

@auth.route('/login',methods = ['GET','POST'])
def login():
  '''
  defines the view for a writer and Reader login
  '''

  render_template('auth/login.html')

@auth.route('/register',methods = ['GET','POST'])
def register():
  form = RegistrationForm()

  if form.validate_on_submit():
    reader = Reader(email = form.email.data, username = form.username.data, password = form.password.data, role_id = 2)
    db.session.add(reader)
    db.session.commit()

    return redirect(url_for('auth,login'))
    title = "New Reader"

  render_template('auth/register.html',registration_form = form)