"""
The flask application package factory:
"""
from flask_bootstrap import Bootstrap
from flask import Flask, request, current_app


app = Flask(__name__)

import edmondsonline.views
