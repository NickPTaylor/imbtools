"""
Tests for app factory.
"""
from app import create_app


def test_config():
    """
    Test automatic and manual configuration.
    """
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing
