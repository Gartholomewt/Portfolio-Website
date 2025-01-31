# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 18:22:31 2025

@author: 15209
"""

from flask import Blueprint, render_template

views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("index.html")