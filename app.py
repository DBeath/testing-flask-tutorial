from application.core import create_app
from application.database import db
from flask_migrate import Migrate

app = create_app('config.py')
migrate = Migrate(app, db)
