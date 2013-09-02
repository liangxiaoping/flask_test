#!/usr/bin/env python

import flask

blueprint = flask.Blueprint('users', __name__)


@blueprint.route('/users/<user_id>', methods=['GET'])
def get_message(user_id):
    context = flask.request.environ.get('context')
    return flask.jsonify(user_id=user_id)

