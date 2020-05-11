from app import create_app,db
from flask_script import Manager,Server,Shell
from app.models import Roles,Comment,Blog,User
from flask_migrate import Migrate,MigrateCommand

#create an app instancea
app = create_app('production')

manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
  '''
  running unit tests
  '''
  import unittest

  tests = unittest.TestLoader().discover('tests')
  unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
  return dict(app = app, db = db, User =User , Comment = Comment, Roles = Roles, Blog = Blog)

if __name__ == '__main__':
  manager.run()