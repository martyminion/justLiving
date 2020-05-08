import os

class Config():
  '''
  sets up the config attributes to be inherited by other config options
  '''
  pass

class ProdConfig(Config):
  '''
  sets up the config attributes for a production environment
  '''
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