#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# kashev.rocks
# Kashev Dalmia - kashev.dalmia@gmail.com

import flask
from flask.ext.assets import Environment, Bundle

app = flask.Flask(__name__)
app.debug=True
assets = Environment(app)

# Register Assets
main_css = Bundle('css/main.scss',
                  filters='scss,cssmin',
                  output='generated/main.css')
assets.register('main_css', main_css)


@app.route("/")
def index():
    return flask.render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
