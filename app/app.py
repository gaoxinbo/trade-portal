#!/usr/bin/env python

import provider

from flask import Flask
from flask import render_template



app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True



p = provider.DataProvider()



@app.route("/")
def index():
  position = p.getCurrentPosition()
  #portion = p.getPortion()
  return render_template("index.html", position=position)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

