"""Test Configuration."""
import pytest

# Flask based imports
from flask.testing import FlaskClient

# API based imports
from api import create_app

# Test based imports
from utils import JSONResponse


@pytest.yield_fixture(scope='session')
def flask_app():
    """Fixture of application creation."""
    app = create_app(environment='testing')
    with app.app_context():
        yield app


@pytest.fixture(scope='session')
def flask_app_client(flask_app):
    """Fixture of application client."""
    flask_app.test_client_class = FlaskClient
    flask_app.response_class = JSONResponse
    return flask_app.test_client()
