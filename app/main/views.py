from flask import render_template,redirect,request,abort
from . import main


@main.route('/')
def index():
  '''
  this will define the view to go to the home page
  '''
  
  title = "Homepage"

  return render_template('index.html',title  = title)