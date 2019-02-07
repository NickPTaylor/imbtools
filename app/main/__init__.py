from flask import Blueprint

BP = Blueprint('main', __name__)

from app.main import routes
