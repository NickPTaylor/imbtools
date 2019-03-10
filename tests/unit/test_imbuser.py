"""
Unit tests for IMB User model.
"""
# pylint: disable=no-self-use,too-few-public-methods,redefined-outer-name

import pytest
from app.models import IMBUser

@pytest.fixture(scope='module')
def imb_user():
    """
    IMB user fixture.
    :return: IMBUser object.
    :rtype: obj
    """
    imb_user = IMBUser(username='jbloggs', name='Joe Bloggs')
    return imb_user


class TestIMBUserModel:
    """
    Unit tests for IMB User model.
    """
    def test_create_new_imbuser(self, imb_user):
        """
        GIVEN an IMBUser user model
        WHEN a new IMBUser model is created
        THEN check the username and name fields are defined correctly
        """
        assert imb_user.username == 'jbloggs'
        assert imb_user.name == 'Joe Bloggs'
        assert repr(imb_user) == '<IMB User jbloggs>'

    def test_check_password(self, imb_user):
        """
        GIVEN an IMBUser user model
        WHEN a new IMBUser password is checked
        THEN True is returned for the correct password and False otherwise
        """
        imb_user.set_password('animbuser1234')
        assert imb_user.check_password('animbuser1234')
        assert not imb_user.check_password('wrongpassword')
