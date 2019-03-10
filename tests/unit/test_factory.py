"""
Unit tests for app factory.
"""
# pylint: disable=no-self-use,too-few-public-methods,redefined-outer-name

from app import create_app


class TestFactory:
    """
    Unit tests for app factory.
    """
    def test_config(self):
        """
        GIVEN a Flask test
        WHEN the factory is invoked
        THEN check that it is in testing mode
        """
        assert not create_app().testing
        config = {
            'TESTING': True,
            'SQLALCHEMY_DATABASE_URI': 'sqlite://:memory:',
            'SQLALCHEMY_TRACK_MODIFICATIONS': False
        }
        assert create_app(config).testing
