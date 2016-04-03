#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# kashev.rocks
# Kashev Dalmia - kashev.dalmia@gmail.com

import flask
from flask.ext.assets import Environment, Bundle

app = flask.Flask(__name__)

assets = Environment(app)

# Register Assets
main_css = Bundle('css/main.scss',
                  filters='scss,cssmin',
                  output='generated/main.css')
assets.register('main_css', main_css)


@app.route("/")
def index():
    return flask.render_template('index.html')


@app.route("/uinstall")
def uinstall():
    uinstall_url = 'https://github.com/kashev/dotfiles/raw/master/uinstall.sh'
    return flask.redirect(uinstall_url)

if __name__ == "__main__":
    app.run(debug=True)
