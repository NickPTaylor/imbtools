"""
Blueprint for hello world.
"""

from flask import Blueprint
from flask_login import login_required

BP = Blueprint('main', __name__)


@BP.route('/')
@BP.route('/index')
@login_required
def index():
    """
    Say hello.

    :return: A greeting.
    :rtype: str
    """
    return "Hello, world"
