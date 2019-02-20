"""
Blueprint for main content.
"""

from flask import Blueprint

BP = Blueprint('main', __name__)

from app.main import routes  # pylint: disable=wrong-import-position
