#!/usr/bin/python
from app import app, db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server

migrate = Migrate(app, db)

manager = Manager(app)
server = Server()

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', server)

if __name__ == '__main__':
    manager.run()
