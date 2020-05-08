from flask import render_template
from . import auth

@auth.route('/login')
def login():
  '''
  defines the view for a writer and Reader login
  '''

  render_template('auth/login.html')
