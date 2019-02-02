"""
IMB tools app.
"""

from flask import Flask

from . import hello


def create_app():
    """
    IMB tools application factory.

    :return: An instance of an IMB tools application.
    :rtype: Flask
    """
    # Create and configure app.
    app = Flask(__name__, instance_relative_config=True)

    # Register blueprints.
    app.register_blueprint(hello.BP)

    return app
