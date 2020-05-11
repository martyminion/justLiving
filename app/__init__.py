from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_simplemde import SimpleMDE
from flask_mail import Mail
from flask_uploads import UploadSet,configure_uploads,IMAGES

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
simple = SimpleMDE()
mail = Mail()
photos = UploadSet('photos',IMAGES)
def create_app(config_name):
  '''
  this is basically where the app is "manufactured" the dependencies are linked and different config options are set
  '''

  app = Flask(__name__)
  

  #creating app configurations

  app.config.from_object(config_options[config_name])

  #initializing flask extensions
  #bootstrap
  bootstrap.init_app(app)
  #db sqlalchemy
  db.init_app(app)
  #login
  login_manager.init_app(app)
  #markdownEditor
  simple.init_app(app)
  #mail
  mail.init_app(app)
  #uploading photos
  configure_uploads(app,photos)
  #Registering a blueprint
  #main
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  #auth
  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

  return app