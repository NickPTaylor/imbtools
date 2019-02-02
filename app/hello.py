"""
Blueprint for hello world.
"""

from flask import Blueprint

BP = Blueprint('hello', __name__)


@BP.route('/')
@BP.route('/index')
def index():
    """
    Say hello.

    :return: A greeting.
    :rtype: str
    """
    return "Hello, world"
