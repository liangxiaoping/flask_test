#!/usr/bin/env python

import flask

blueprint = flask.Blueprint('messages', __name__)


@blueprint.route('/messages/<message_id>', methods=['GET'])
def get_message(message_id):
    context = flask.request.environ.get('context')
    return flask.jsonify(message_id=message_id)

