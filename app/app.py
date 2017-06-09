#!/usr/bin/env python

import provider

from functools import wraps
from flask import Flask
from flask import render_template
from flask import request 
from flask import current_app 
from flask_restful import Resource, Api


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


api = Api(app)
p = provider.DataProvider()


def jsonp(func):
    """Wraps JSONified output for JSONP requests."""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            data = str(func(*args, **kwargs))
            content = str(callback) + '(' + data + ')'
            mimetype = 'application/javascript'
            return current_app.response_class(content, mimetype=mimetype)
        else:
            return func(*args, **kwargs)
    return decorated_function

class getPosition(Resource):
    @jsonp
    def get(self):
        return p.getCurrentPosition()

api.add_resource(getPosition, '/position')





if __name__ == '__main__':
    app.run(host='0.0.0.0')




