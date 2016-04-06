#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# kashev.rocks
# Kashev Dalmia - kashev.dalmia@gmail.com

import logging

import flask

from .assets import register_assets
# Import the links which go on the home page
from .home_page_links import LINKS

app = flask.Flask(__name__)

# Set up logging.
logging.basicConfig(filename='debug.log', level=logging.DEBUG)


# Configure all the URLS


@app.route("/")
def index():
    """ Return the main page for kashev.rocks. """
    return flask.render_template('index.html', links=LINKS)


@app.route("/resume")
def resume():
    """ Send a PDF of my resume. """
    return flask.send_from_directory(
        app.static_folder, 'pdf/Kashev_Dalmia_Resume_v2015_08_0sx.pdf')


@app.route("/uinstall")
def uinstall():
    """ Return the url to my Ubuntu Installer script. For Curling;
            `curl -L kashev.rocks/uinstall`
    """
    uinstall_url = 'https://github.com/kashev/dotfiles/raw/master/uinstall.sh'
    return flask.redirect(uinstall_url)


if __name__ == "__main__":
    app.debug = True
    register_assets(app)
    app.run()
