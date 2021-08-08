import pytest
from flask import Flask
from pallets.app import create_app


@pytest.fixture(scope='session')
def app():
    """
    Setup our flask test app fixture, this only gets executed once.

    :return: Flask app
    """
    params = {
        "DEBUG": False,
        "TESTING": True,
        "SERVER_NAME": "pallets.example",
    }

    _app = create_app(settings_override=params)

    # Establish an application context before running the tests.
    ctx = _app.app_context()
    ctx.push()
    yield _app
    ctx.pop()


@pytest.fixture(scope='function')
def client(app: Flask):
    """
    Setup an app client, this gets executed for each test function.

    :param app: Pytest fixture
    :return: Flask app client
    """
    yield app.test_client()
