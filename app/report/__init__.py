"""
Blueprint for rota reports.
"""

from flask import Blueprint

BP = Blueprint('report', __name__)

from app.report import routes  # pylint: disable=wrong-import-position
