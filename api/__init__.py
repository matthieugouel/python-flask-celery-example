"""Initialization module of the package."""
# Flask based imports
from flask import Flask

# Celery based imports
from celery import Celery

# API configuration imports
from api.config import Config, config

# System based imports
import os

# Version handling
import pkg_resources

try:
    # If the app is packaged
    # Get the version of the setup package
    __version__ = pkg_resources.get_distribution('api').version
except pkg_resources.DistributionNotFound:  # pragma: no cover
    # If app is not used as a package
    # Hardcoded configuration version
    __version__ = Config.VERSION


class Factory(object):
    """Factory of the instance."""

    def __init__(self, environment='default'):
        """Instantiate flask and celery instance."""
        # Get the running environment
        self._environment = os.getenv("APP_ENVIRONMENT")
        if not self._environment:
            self._environment = environment

        # Configuration constants
        self.config = config

        # Flask instantiation
        self._flask = Flask(__name__)

        # Celery instantiation
        self._celery = Celery(__name__)

        # Configure the application
        self._configure_app()

    def _configure_app(self):
        """Configure the application."""
        # Flask configuration
        self.flask.config.from_object(self.config[self._environment])

        # Swagger documentation
        self.flask.config.SWAGGER_UI_DOC_EXPANSION = 'list'
        self.flask.config.SWAGGER_UI_JSONEDITOR = True

        # Celery Configuration
        self.celery.conf.update(self.flask.config)

    @property
    def environment(self):
        """Getter for environment attribute."""
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Setter for environment attribute."""
        # Change the environment
        self._environment = environment

        # Update applcation settings
        self._configure_app()

    @property
    def flask(self):
        """Getter of flask instance."""
        return self._flask

    @property
    def celery(self):
        """Getter of celery instance."""
        return self._celery

    def register(self, blueprint):
        """Register a specified blueprint."""
        self.flask.register_blueprint(blueprint)


# Instantiation of the factory
factory = Factory()

# Ignore `module level import not at top of file` warning
# pylama: ignore=E402

# API Resources imports
from api.resources import blueprint

# Register the blueprint
factory.register(blueprint)


__all__ = ['Factory', 'HelloWorld', 'ByeWorld']
