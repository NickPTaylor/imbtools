"""
Blueprint for hello world.
"""
from app.main import BP

@BP.route('/')
@BP.route('/index')
def index():
    """
    Say hello.

    :return: A greeting.
    :rtype: str
    """
    return "Hello, world"
