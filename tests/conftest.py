"""
Unit test configuration.
"""

# pylint: disable=redefined-outer-name
import pytest

from flask import url_for

from app import create_app, DB
from app.models import IMBUser


class AuthenticationActions:
    """
    Provide methods for authenticating user in tests.
    """
    def __init__(self, client):
        self._client = client

    def login(self, login_data, **kwargs):
        """
        Login client.

        :param login_data: Dictionary with username and password keys
        :type login_data: dict
        :param kwargs: Extra arguments.
        :type kwargs: dict
        :return: Request to login user.
        """
        return self._client.post(
            url_for('auth.login', **kwargs),
            data=login_data,
            follow_redirects=True
        )

    def logout(self):
        """
        Logout user.

        :return: Request to logout user.
        """
        return self._client.get(
            url_for('auth.logout'),
            follow_redirects=True
        )


@pytest.fixture(scope='module')
def testing_app():
    """
    Fixture to setup test app context.
    """
    config = {
        'BCRYPT_LOG_ROUNDS': 4,
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite://',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'SECRET_KEY': 'test',
        'WTF_CSRF_ENABLED': False
    }

    # Setup.
    app = create_app(config)
    app_ctx = app.app_context()
    req_ctx = app.test_request_context()
    app_ctx.push()
    req_ctx.push()

    # Yield app instance.
    yield app

    # Tear down.
    req_ctx.push()
    app_ctx.pop()


@pytest.fixture(scope='module')
def testing_client(testing_app):
    """
    Fixture to setup test client context.

    :param testing_app: Test app context.
    :type testing_app: object
    :return: object
    """
    return testing_app.test_client()


@pytest.fixture(scope='module')
def init_database(testing_app):  # pylint: disable=unused-argument
    """
    Fixture to initialise database with a user.

    :param testing_app: Test app context.
    :type testing_app: object
    :return:
    """
    # Setup.
    DB.create_all()
    joe = IMBUser(
        username='jbloggs',
        password_hash=('pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e33'
                       '64c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f')
    )
    DB.session.add(joe)
    DB.session.commit()

    # Yield DB instance.
    yield DB

    # Tear down.
    DB.drop_all()


@pytest.fixture(scope='function')
def auth(testing_client):
    """
    Fixture to provide authentication methods.
    :param testing_client: Test client context.
    :type testing_client: object
    :return: Object with methods for authentication.
    """
    auth_obj = AuthenticationActions(testing_client)
    yield auth_obj
    auth_obj.logout()


@pytest.fixture
def cli_runner(testing_app):
    """
    Test CLI runner.

    :param testing_app: Test CLI runner for app instance.
    :return: object
    """
    return testing_app.test_cli_runner()
