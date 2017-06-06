#!/usr/bin/env python

import logging
import provider

from flask import Flask
from flask import render_template



app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

logger = logging.getLogger('werkzeug')
handler = logging.FileHandler('access.log')
logger.addHandler(handler)


p = provider.DataProvider()



@app.route("/")
def index():
  position = p.getCurrentPosition()
  return render_template("index.html", position=position)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

