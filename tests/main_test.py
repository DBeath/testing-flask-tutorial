from flask import url_for
from application.frontend.views import add
from application.frontend.models import User, users_schema
from application.database import db


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


def test_not_found(client):
    response = client.get('/notfound')
    assert response.status_code == 404


def test_add_integers():
    result = add(1, 2)
    assert result == 3


def test_add_strings():
    result = add('1', '2')
    assert result == 3


def test_add_integer_and_string():
    result = add('1', 2)
    assert result == 3


def test_add_view_returns_result(client):
    url = url_for('frontend.add_view', input1=1, input2=2)

    response = client.post(url)

    assert response.status_code == 200

    assert type(response.get_data()) is bytes

    assert int(response.get_data()) == 3


def test_add_view_returns_400(client):
    url = url_for('frontend.add_view', input1=1)

    response = client.post(url)

    assert response.status_code == 400


def test_get_all_users(client, session):
    user1 = User(name='Test User 1')
    user2 = User(name='Test User 2')

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    url = url_for('frontend.get_users')

    response = client.get(url)

    assert response.status_code == 200

    json_users = response.get_data()
    print(json_users)

    users = users_schema.load(json_users, session=db.session).data
    print(users)
    assert False


def test_create_user(client, session):
    user_name = 'Test User'

    url = url_for('frontend.create_user')

    params = {'name': user_name}
    response = client.post(url, data=params)

    assert response.status_code == 200
    print(response.get_data())

    assert False
