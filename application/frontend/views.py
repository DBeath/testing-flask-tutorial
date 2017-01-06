from application.frontend import frontend_blueprint as bp
from flask import request, make_response, abort, Response
from application.frontend.models import User
from application.database import db


@bp.route('/')
def index():
    return 'Hello World!'


def add(a, b):
    return int(a) + int(b)


@bp.route('/add', methods=['POST'])
def add_view():
    a = request.args.get('input1')
    b = request.args.get('input2')
    if not a or not b:
        return abort(400)

    result = add(a, b)
    return make_response(str(result))


@bp.route('/users')
def get_users():
    users = User.query.all()
    return users

@bp.route('/users', methods=['POST'])
def create_user():
    name = request.args.get('name')
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return user

@bp.route('/users/<int:user_id>', methods=['GET', 'POST'])
def single_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        abort(204)

    if request.methods == 'POST':
        name = request.args.get('name')
        user.name = name
        db.session.commit()

    return user

@bp.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return Response(status_code=200)
