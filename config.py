import os

class Config():
  '''
  sets up the config attributes to be inherited by other config options
  '''
  SECRET_KEY = os.environ.get('SECRET_KEY') 
  #configs for SimpleMDE

  SIMPLEMDE_JS_IIFE = True
  SIMPLEMDE_USE_CDN = True

  #email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
  MAIL_DEFAULT_SENDER = 'wawerulawrence@gmail.com'
  #random quote api config

  RANDOM_QUOTE_URL = "http://quotes.stormconsultancy.co.uk/random.json"
  #destination for photos
  UPLOADED_PHOTOS_DEST = 'app/static/photos'

class ProdConfig(Config):
  '''
  sets up the config attributes for a production environment
  '''
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
  DEBUG = False

class DevConfig(Config):
  '''
  sets up the config attributes for development environment
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martin:kimani@localhost/blog'
  DEBUG = True

class TestConfig(Config):
  '''
  sets up the config options for tests
  '''

  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martin:kimani@localhost/blog_test'

config_options = {
  "development":DevConfig,
  "production":ProdConfig,
  "test":TestConfig}