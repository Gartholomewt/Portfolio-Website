# -*- coding: utf-8 -*-
"""
Created Jan 31, 2025

@author: Gary Tyree
"""

from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)