"""
Functional tests for user authentication.
"""
# pylint: disable=no-self-use,too-few-public-methods,redefined-outer-name

import pytest
from flask import session, request, url_for
from flask_login import current_user

LOGIN_DATA = {'username': 'jbloggs', 'password': 'test'}


@pytest.mark.usefixtures('init_database')
class TestAuthentication:
    """
    Functional tests for user authentication.
    """

    def test_login_fixture(self, testing_client, auth):
        """
        GIVEN a Flask application
        WHEN the login fixture is use
        THEN the user is authenticated and redirected properly.
        """

        # To start with, user is anonymous.
        assert current_user.is_anonymous

        with testing_client:

            auth.login(LOGIN_DATA)

            # Test flask_login plugin.
            assert current_user.is_authenticated
            assert current_user.username == 'jbloggs'

            # user_id should now be in session.
            assert 'user_id' in session

            # Test app behaviour.
            assert request.endpoint == 'main.index'
            assert 'Logged in successfully' in session['_flashes'][0]

            # Check that user now has access to protected pages.
            response = testing_client.get(url_for('report.compose_report'),
                                          follow_redirects=True)
            assert request.endpoint == 'report.compose_report'
            assert b'Compose Rota Report' in response.data

    def test_logout_fixture(self, testing_client, auth):
        """
        GIVEN a Flask application
        WHEN the logout fixture is use
        THEN the user is unauthenticated and redirected to login.
        """

        with testing_client:
            # Login
            auth.login(LOGIN_DATA)
            assert current_user.is_authenticated

            # Logout.
            auth.logout()
            assert current_user.is_anonymous

            # user_id should NOT be in session.
            assert 'user_id' not in session

            # Test app behaviour
            assert request.endpoint == 'auth.login'

            # Check that user does not have access to protected pages.
            response = testing_client.get(url_for('report.compose_report'),
                                          follow_redirects=True)
            assert request.endpoint == 'auth.login'
            assert b'Sign In' in response.data

    def test_login_page(self, testing_client):
        """
        GIVEN a Flask application
        WHEN viewing '/login' page
        THEN check response is valid
        """
        # View login page.
        with testing_client:
            response = testing_client.get(url_for('auth.login'))
            assert request.endpoint == 'auth.login'
            assert response.status_code == 200
            assert b"IMB Tools - Sign In" in response.data

    def test_login_when_authenticated(self, testing_client, auth):
        """
        GIVEN a Flask application
        WHEN the '/login' page is viewed and user is authenticated
        THEN check redirect to index.
        """
        with testing_client:
            auth.login(LOGIN_DATA)
            response = testing_client.get(url_for('auth.login'),
                                          follow_redirects=True)
            assert request.endpoint == 'main.index'
            assert response.status_code == 200

    @pytest.mark.parametrize(('username', 'password'), [
        ('jbloggs', 'wrong'),
        ('joebloggs', 'test'),
    ])
    def test_login_with_incorrect_credentials(self, testing_client, auth,
                                              username, password):
        """
        GIVEN a Flask application
        WHEN the '/login' page is submitted with incorrect credentials
        THEN check flashed message and correct response
        """
        with testing_client:
            # Login in with incorrect credentials.
            response = auth.login({'username': username, 'password': password})
            assert b'Invalid' in response.data
            assert request.endpoint == 'auth.login'

            # Ensure no access pages requiring authentication.
            testing_client.get(url_for('main.index'))
            assert b"IMB Tools - Sign In" in response.data

    @pytest.mark.parametrize(('username', 'password'), [
        ('', 'test'),
        ('jbloggs', ''),
    ])
    def test_invalid_login_submit(self, testing_client, auth,
                                  username, password):
        """
        GIVEN a Flask application
        WHEN the '/login' page is submitted with an invalid fields
        THEN check login page still shows
        """
        with testing_client:
            # Login in with incorrect credentials.
            response = auth.login({'username': username, 'password': password})
            assert b"IMB Tools - Sign In" in response.data
            assert request.endpoint == 'auth.login'

            # Ensure no access pages requiring authentication.
            testing_client.get(url_for('main.index'))
            assert b"IMB Tools - Sign In" in response.data

    def test_login_with_next(self, testing_client, auth):
        """
        GIVEN a Flask application
        WHEN a next page is passed as argument to login
        THEN check redirect to next page on successful login
        """
        with testing_client:
            # Login in with incorrect credentials.
            response = auth.login(LOGIN_DATA,
                                  next=url_for('report.compose_report'))
            assert request.endpoint == 'report.compose_report'
            assert b'Compose Rota Report' in response.data

    def test_login_with_invalid_next(self, testing_client, auth):
        """
        GIVEN a Flask application
        WHEN a next page is passed that is an external website
        THEN check redirect to index
        """
        with testing_client:
            # Login in with incorrect credentials.
            auth.login(LOGIN_DATA, next='https://www.example.com')
            assert request.endpoint == 'main.index'
