# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 17:23:20 2025

@author: 15209
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"