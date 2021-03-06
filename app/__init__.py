"""
IMB tools app.
"""

import pkg_resources
__version__ = pkg_resources.get_distribution('imbtools').version

from flask import Flask

from app.main import MAIN_BP
from app.auth import AUTH_BP
from app.report import ROTA_REPORT_BP
from app.models import DB, MIGRATE, LOGIN_MANAGER
from app.models import IMBUser, Visit
from config import Config


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

    DB.init_app(app)
    MIGRATE.init_app(app, DB)

    LOGIN_MANAGER.login_view = 'auth.login'
    LOGIN_MANAGER.init_app(app)

    # Register blueprints.
    app.register_blueprint(MAIN_BP)
    app.register_blueprint(ROTA_REPORT_BP, url_prefix='/report')
    app.register_blueprint(AUTH_BP, url_prefix='/auth')

    return app


APP = create_app()


@APP.shell_context_processor
def shell_context():  # pragma: no cover
    """
    Make shell context.

    :return: A dictionary of objects for use in shell context.
    :rtype: dict
    """
    return {'DB': DB, 'IMBUser': IMBUser, 'Visit': Visit}
