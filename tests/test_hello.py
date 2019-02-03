"""
Tests for greeting.
"""


def test_hello(client):
    """
    Test that the response is 'Hello, world'.

    :param client: Client for running unit tests.
    """
    response = client.get('/')
    assert response.data == b'Hello, world'
