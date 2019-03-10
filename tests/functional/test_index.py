"""
Function tests for index.
"""
# pylint: disable=no-self-use,too-few-public-methods,redefined-outer-name

import pytest
from flask import url_for

LOGIN_DATA = {'username': 'jbloggs', 'password': 'test'}


@pytest.mark.usefixtures('init_database')
class TestIndex:
    """
    Function tests for index.
    """
    def test_index(self, testing_client, auth):
        """
        GIVEN a Flask app
        WHEN index is view
        THEN check that response is correct
        """

        auth.login(LOGIN_DATA)
        response = testing_client.get(url_for('main.index'))
        assert response.status_code == 200
        assert response.data == b'Hello, world'
