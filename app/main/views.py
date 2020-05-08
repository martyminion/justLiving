from flask import render_template,redirect,request



def index():
  '''
  this will define the view to go to the home page
  '''

  title = "Homepage"

  render_template('index.html',title  = title)