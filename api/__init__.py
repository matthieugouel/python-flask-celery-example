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
        """Instanciate flask and celery instance."""
        # Get the running environment
        self.__environment = os.getenv("APP_ENVIRONMENT")
        if not self.__environment:
            self.__environment = environment

        # Configuration constants
        self.config = config

        # Flask instantiation
        self.__app = Flask(__name__)

        # Celery instantiation
        self.__celery = Celery(__name__)

        # Flask configuration
        self.__app.config.from_object(self.config[self.__environment])

        # Swagger documentation
        self.__app.config.SWAGGER_UI_DOC_EXPANSION = 'list'
        self.__app.config.SWAGGER_UI_JSONEDITOR = True

        # Celery Configuration
        self.__celery.conf.update(self.__app.config)

    @property
    def environment(self):
        """Getter of environment variable."""
        return self.__environment

    @environment.setter
    def environment(self, environment):
        """Setter of environment variable."""
        self.__environment = environment

    @property
    def flask(self):
        """Getter of flask instance."""
        return self.__app

    @property
    def celery(self):
        """Getter of celery instance."""
        return self.__celery

    def register(self, blueprint):
        """Register a specified blueprint."""
        self.__app.register_blueprint(blueprint)


# Instantiation of the factory
factory = Factory()

# Ignore `module level import not at top of file` warning
# pylama: ignore=E402

# API Resources imports
from api.resources import blueprint

# Register the blueprint
factory.register(blueprint)


__all__ = ('Factory', 'HelloWorld')
