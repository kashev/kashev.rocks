#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# kashev.rocks
# Kashev Dalmia - kashev.dalmia@gmail.com

import sys

activate_this = '/home/kashev/.virtualenvs/kashev.rocks/bin/activate_this.py'
with open(activate_this) as f:
    code = compile(f.read(), activate_this, 'exec')
    exec(code)

sys.path.insert(0, '/srv/kashev.rocks/')

# Import the WSGI application. mod_wsgi expects it to be called `application`.
from src.kashevrocks import app as application
from src.assets import register_assets
register_assets(application)
