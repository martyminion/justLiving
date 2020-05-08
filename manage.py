from app import create_app,db
from flask_script import Manager,Server,Shell
from app.models import Writer,Reader,Roles,Comment,Blog

#create an app instancea
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

@manager.shell
def make_shell_context():
  return dict(app = app, db = db, Writer = Writer, Reader = Reader, Comment = Comment, Roles = Roles, Blog = Blog)

if __name__ == '__main__':
  manager.run()