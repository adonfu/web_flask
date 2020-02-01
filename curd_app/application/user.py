# -*- coding: utf-8 -*-

from flask import Blueprint


user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/')
def index():
    return "User's Index page"
