"""
Models for app.
"""
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

DB = SQLAlchemy()
MIGRATE = Migrate()


class IMBMember(DB.Model):  # pylint: disable=too-few-public-methods
    """
    IMB member model.
    """
    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(64), index=True, unique=True)
    name = DB.Column(DB.String(64), index=True, unique=True)
    password_hash = DB.Column(DB.String(128))
    visits = DB.relationship('Visit', backref='visitor', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Visit(DB.Model):  # pylint: disable=too-few-public-methods
    """
    Visit model.
    """
    id = DB.Column(DB.Integer, primary_key=True)
    imb_member = DB.Column(DB.Integer, DB.ForeignKey('imb_member.id'))
    created = DB.Column(DB.DateTime, index=True, default=datetime.utcnow)
    visit_date = DB.Column(DB.Date, index=True)
    visit_start = DB.Column(DB.Time)
    visit_finish = DB.Column(DB.Time)
