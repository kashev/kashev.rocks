#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# kashev.rocks
# Kashev Dalmia - kashev.dalmia@gmail.com

from flask.ext.script import Manager
from flask.ext.assets import ManageAssets

from src.kashevrocks import app
from src.assets import register_assets

manager = Manager(app)

assets_env = register_assets(app)
manager.add_command("assets", ManageAssets(assets_env))


@manager.command
def liveserver(debug=True):
    """ Runs a live reloading server which watches non-python code as well. """
    import livereload
    app.debug = debug
    assets_env.debug = debug
    server = livereload.Server(app.wsgi_app)

    server.watch('src/')

    server.serve()


@manager.command
def clean():
    """ Cleans up all generated and cache files from the project. """
    import shutil
    paths_to_clean = ['src/static/.webassets-cache',
                      'src/static/generated']
    for path in paths_to_clean:
        try:
            shutil.rmtree(path)

        except FileNotFoundError:
            pass  # They're not there, that's fine.


if __name__ == "__main__":
    manager.run()
