"""
ROUTES FOR EDMONDS ONLINE
"""
import os
from flask import render_template, Flask
from flask import current_app as app
from .nav import nav


@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html',
        nav=nav
    )
