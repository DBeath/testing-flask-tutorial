import pytest
from application.core import create_app

@pytest.fixture(scope='session')
def app():
    app = create_app('config.py')
    app.config['TESTING'] = True

    ctx = app.test_request_context()
    ctx.push()

    yield app

    ctx.pop()

@pytest.fixture(scope='function')
def client(app):
    with app.test_client() as client:
        yield client
