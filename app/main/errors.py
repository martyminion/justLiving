from flask import render_template
from . import main

@main.errorhandler(404)
def fourowfour(error):
  '''
  function to render a 404 error page when it occurs
  '''
  return render_template('error.html'),404