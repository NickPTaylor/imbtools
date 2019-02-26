"""
Unit test configuration.
"""
import pytest

from app import create_app

@pytest.fixture
def test_app():
    """
    Invoke app factory.
    """
    config = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite://:memory:',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    }
    app = create_app(config)
    yield app

@pytest.fixture
def client(test_app):  # pylint: disable=redefined-outer-name
    """
    Client for running unit tests.

    :param test_app: Test client of an app instance
    :return: object
    """
    return test_app.test_client()

@pytest.fixture
def runner(test_app):  # pylint: disable=redefined-outer-name
    """
    Test CLI runner.

    :param test_app: Test CLI runner for app instance.
    :return: object
    """
    return test_app.test_cli_runner()
