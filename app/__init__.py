"""
IMB tools app.
"""

import pkg_resources

from flask import Flask

from app.main import BP as MAIN_BP
from app.report import BP as ROTA_REPORT_BP

from config import Config

__version__ = pkg_resources.get_distribution('imbtools').version


def create_app(test_config=None):
    """
    IMB tools application factory.

    :param test_config: App configuration variables.
    :type: dict
    :return: An instance of an IMB tools application.
    :rtype: Flask
    """
    # Create and configure app.
    app = Flask(__name__, instance_relative_config=True)

    # Get configuration.
    if test_config is None:
        app.config.from_object(Config)
    else:
        app.config.from_mapping(test_config)

    # Register blueprints.
    app.register_blueprint(MAIN_BP)
    app.register_blueprint(ROTA_REPORT_BP, url_prefix='/report')
    return app
