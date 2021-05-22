from flask import Flask
from os import path
from flask import request
from flask import jsonify
from flask import render_template
from datetime import date
from datetime import timedelta


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

    return app