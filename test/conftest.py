"""Test Configuration."""
# Test package used
import pytest

# Flask based imports
from flask.testing import FlaskClient

# API based imports
from api import Factory
from api.resources import blueprint

# Test based imports
from utils import JSONResponse


@pytest.yield_fixture(scope='session')
def factory_app():
    """Fixture of factory with testing environment."""
    yield Factory(environment='testing')


@pytest.yield_fixture(scope='session')
def flask_app(factory_app):
    """Fixture of application creation."""
    app = factory_app.set_flask()
    factory_app.register(blueprint)
    with app.app_context():
        yield app


@pytest.yield_fixture(scope='session')
def celery_app(factory_app):
    """Fixture of celery instance creation."""
    yield factory_app.set_celery()


@pytest.fixture(scope='session')
def flask_app_client(flask_app):
    """Fixture of application client."""
    flask_app.test_client_class = FlaskClient
    flask_app.response_class = JSONResponse
    return flask_app.test_client()
