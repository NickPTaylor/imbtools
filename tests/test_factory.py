"""
Tests for app factory.
"""
from app import create_app


def test_config():
    """
    Test automatic and manual configuration.
    """
    assert not create_app().testing
    config = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite://:memory:',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    }
    assert create_app(config).testing
