"""this is init module"""

from flask import Flask

""" place where app is defined"""
app = Flask(__name__)

from app import model 


