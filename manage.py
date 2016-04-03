#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# kashev.rocks
# Kashev Dalmia - kashev.dalmia@gmail.com

from flask.ext.script import Manager

from src.app import app

manager = Manager(app)


@manager.command
def hello(name='Kashev'):
    """ Just say hello. """
    print("Hello, {}! You're doing a good job.".format(name))


@manager.command
def liveserver(debug=True):
    """ Runs a live reloading server which watches non-python code as well. """
    import livereload
    app.debug = debug
    server = livereload.Server(app.wsgi_app)

    server.watch('src/')

    server.serve()


if __name__ == "__main__":
    manager.run()
