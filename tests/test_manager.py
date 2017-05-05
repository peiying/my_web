from flask_script import Server, Manager
from . import create_app

manager = Manager(create_app)
manager.add_command("runserver", Server())

if __name__ == "__main__":
    manager.run()