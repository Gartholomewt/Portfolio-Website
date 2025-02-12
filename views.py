# -*- coding: utf-8 -*-
"""
Created on Jan 29, 2025

@author: 15209
"""

from flask import Blueprint, render_template

views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("index2.html")

@views.route("/Resume")
def resume():
    return render_template("index2.html")