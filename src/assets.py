#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# kashev.rocks
# Kashev Dalmia - kashev.dalmia@gmail.com

from flask.ext.assets import Environment, Bundle, Jinja2Filter

# Import the links which go on the home page
from .home_page_links import LINKS


def register_assets(app):
    """ Given a Flask app, register all the assets for it. """
    assets_env = Environment(app)
    assets_env.debug = app.debug

    main_css = Bundle('css/main.jinja.scss',
                      filters=[Jinja2Filter(context={'links': LINKS}),
                               'scss',
                               # 'pyscss',  # Choose pyscss or scss, not both.
                               'cssmin'
                               ],
                      output='generated/main.css')
    assets_env.register('main_css', main_css)

    main_js = Bundle('js/main.js',
                     filters='jsmin',
                     output='generated/main.min.js')
    assets_env.register('main_js', main_js)

    return assets_env
