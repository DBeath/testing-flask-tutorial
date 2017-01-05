from flask import Flask
from application.frontend import frontend_blueprint

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_pyfile(config_name)

    app.register_blueprint(frontend_blueprint)

    print("Created app {0}".format(app.config['PROJECT_NAME']))
    return app
