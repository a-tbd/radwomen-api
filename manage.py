from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import create_app
from app.models import db
from app.models.radwomen import Radwoman




app = create_app()


manager = Manager(app)
migrate = Migrate(app, db)

# Migrations
manager.add_command('db', MigrateCommand)

@manager.option('-n', '--name', help='add the wikipedia name')
@manager.option('-l', '--link', help='add the wikipedia link', default=None)
def new_radwoman(name, link):

    

    print(Radwoman.query.all())

    try:
        newRadWoman = Radwoman(name=name)
        if link:
            newRadWoman.wiki_link = link
        db.session.add(newRadWoman)
        db.session.commit()
    except Exception as e:
        raise(e)


@manager.shell
def make_shell_context():
    return dict(
        app=app,
        db=db,
        # add models
        Radwoman=Radwoman
        
    )
if __name__ == '__main__':
    manager.run()
