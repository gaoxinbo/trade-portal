#!/usr/bin/env python

import provider

from flask import Flask
from flask import render_template
from flask_restful import Resource, Api


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


api = Api(app)
p = provider.DataProvider()

class getPosition(Resource):
    def get(self):
        return p.getCurrentPosition()

api.add_resource(getPosition, '/position')




@app.route("/")
def index():
  #portion = p.getPortion()
  return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')

