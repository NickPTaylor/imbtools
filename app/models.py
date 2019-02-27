"""
Models for app.
"""
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
DB = SQLAlchemy()
MIGRATE = Migrate()


class IMBUser(DB.Model):
    """
    IMB member model.
    """
    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(64), index=True, unique=True)
    name = DB.Column(DB.String(64), index=True, unique=True)
    password_hash = DB.Column(DB.String(128))
    visits = DB.relationship('Visit', backref='visitor', lazy='dynamic')

    def set_password(self, password):
        """
        Set password_hash property.

        :param password: Plaintext version of password
        :type password: str
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Check hashed password matches password_hash.
        :param password: Plain text password.
        :type password: str
        :return: Does the password match the hash?
        :rtype: bool
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<IMB User {}>'.format(self.username)


class Visit(DB.Model):  # pylint: disable=too-few-public-methods
    """
    Visit model.
    """
    id = DB.Column(DB.Integer, primary_key=True)
    imb_user = DB.Column(DB.Integer, DB.ForeignKey('imb_user.id'))
    created = DB.Column(DB.DateTime, index=True, default=datetime.utcnow)
    visit_date = DB.Column(DB.Date, index=True)
    visit_start = DB.Column(DB.Time)
    visit_finish = DB.Column(DB.Time)
