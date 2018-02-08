"""Resources Test Configuration."""
import pytest

# Flask based imports
from flask.testing import FlaskClient

# API based imports
from api import Factory
from api.resources import blueprint

# Test based imports
from .utils import JSONResponse

# API asynchronous tasks based imports
# Using resources classes directly will use factory
# So we have to import it to set the environment to `testing`
from api import factory
from api.resources.main import ByeWorld

# Set the factory environment to `testing`
factory.environment = 'testing'


@pytest.yield_fixture(scope='session')
def factory_app():
    """Fixture of factory with testing environment."""
    yield Factory(environment='testing')


@pytest.yield_fixture(scope='session')
def flask_app(factory_app):
    """Fixture of application creation."""
    factory_app.set_flask()
    factory_app.register(blueprint)
    yield factory_app


@pytest.yield_fixture(scope='session')
def celery_app(factory_app):
    """Fixture of celery instance creation."""
    factory_app.set_flask()
    factory_app.register(blueprint)
    factory_app.set_celery()
    yield factory_app


@pytest.fixture(scope='session')
def flask_app_client(flask_app):
    """Fixture of application client."""
    app = flask_app.flask
    app.test_client_class = FlaskClient
    app.response_class = JSONResponse
    return app.test_client()


@pytest.yield_fixture(scope='session')
def byeworld(celery_app):
    """Fixture of ByeWorld resource."""
    return ByeWorld()
