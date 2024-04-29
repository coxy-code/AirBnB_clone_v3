#!/usr/bin/python3
""" Flask Application """

from flask import Blueprint

app_view = Blueprint('app_view',__name__,url_prefix='app/vi')

from app.v1.views.index import *