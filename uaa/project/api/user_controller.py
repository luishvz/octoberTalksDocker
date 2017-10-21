# Import flask dependencies
from flask import Blueprint, jsonify, request

# request, render_template, flash, g, session, redirect, url_for

from ..services import user_service
from ..schema.user_schema import user_schema, users_schema

user_controller = Blueprint('users', __name__, url_prefix='/users')


# Set the route and accepted methods

@user_controller.route('', methods=['GET'])
def get_all_users():
    # all_users = user_service.get_all_users()
    # return users_schema.jsonify(all_users), 200
    return jsonify({
        'hola': 'mundo'
    })

@user_controller.route('/add', methods=['POST'])
def add_user():
    post_data = request.get_json()

    if not post_data or 'username' not in request.args or 'email' not in request.args:
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload'
        }
        return jsonify(response_object), 400

    username = post_data['username']
    email = post_data['email']
    try:
        new_user = user_service.add_user(username, email)
        return user_schema.jsonify(new_user), 200
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': e.args[0]
        }
        return jsonify(response_object), 500
