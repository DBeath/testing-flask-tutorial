import pytest
from application.core import create_app
from application.database import db as _db


@pytest.fixture(scope='session')
def app():
    app = create_app('test_config.py')
    app.config['TESTING'] = True

    ctx = app.test_request_context()
    ctx.push()

    yield app

    ctx.pop()


@pytest.fixture(scope='function')
def client(app):
    with app.test_client() as client:
        yield client


@pytest.fixture(scope='session')
def db(app):
    _db.drop_all()
    _db.create_all()

    yield _db

    _db.session.remove()
    _db.drop_all()


@pytest.fixture(scope='function')
def session(db, app):
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    yield session

    transaction.rollback()
    connection.close()
    session.remove()
