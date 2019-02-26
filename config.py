"""
Configuration for app.
"""
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config:  # pylint: disable=too-few-public-methods
    """
    Configuration object.
    """
    # Security.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Database.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASEDIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
