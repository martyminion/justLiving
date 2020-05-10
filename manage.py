from app import create_app,db
from flask_script import Manager,Server,Shell
from app.models import Reader,Roles,Comment,Blog,Writer
from flask_migrate import Migrate,MigrateCommand

#create an app instancea
app = create_app('development')

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)
@manager.shell
def make_shell_context():
  return dict(app = app, db = db, Writer = Writer, Reader = Reader, Comment = Comment, Roles = Roles, Blog = Blog)

if __name__ == '__main__':
  manager.run()