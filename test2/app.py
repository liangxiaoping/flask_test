#!/usr/bin/env python

import sys
import flask

sys.path.append('~/workspace/flask_test/test2')

from users import blueprint as users
from messages import blueprint as messages

app = flask.Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(users)
    app.register_blueprint(messages)
    app.run()