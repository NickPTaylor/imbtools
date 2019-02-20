"""
Configuration for app.
"""
import os


class Config:  # pylint: disable=too-few-public-methods
    """
    Configuration object.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
