from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
  '''
  this is basically where the app is "manufactured" the dependencies are linked and different config options are set
  '''

  app = Flask(__name__)
  

  #creating app configurations

  app.config.from_object(config_options[config_name])

  #initializing flask extensions
  bootstrap.init_app(app)

  #Registering a blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  return app