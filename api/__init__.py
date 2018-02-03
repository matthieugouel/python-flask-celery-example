"""Initialization module of the package."""
# Flask based imports
from flask import Flask

# Plugins based imports


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
    # Hardcode the version from the configuration file
    __version__ = Config.VERSION


class Factory(object):
    """Factory of the api."""

    def __init__(self, environment='default'):
        """Initialize Factory with the proper environment."""
        # Get the running environment
        self._environment = os.getenv("APP_ENVIRONMENT")
        if not self._environment:
            self._environment = environment

    @property
    def environment(self):
        """Getter for environment attribute."""
        return self._environment

    def set_flask(self, **kwargs):
        """Flask instantiation."""
        # Flask instance creation
        self.flask = Flask(__name__, **kwargs)

        # Flask configuration
        self.flask.config.from_object(config[self._environment])

        # Swagger documentation
        self.flask.config.SWAGGER_UI_DOC_EXPANSION = 'list'
        self.flask.config.SWAGGER_UI_JSONEDITOR = True

        return self.flask

    def register(self, blueprint):
        """Register a specified blueprint."""
        self.flask.register_blueprint(blueprint)


# Instantiation of the factory
factory = Factory()

# Enable flask instance
factory.set_flask()

# Enable of the desired plugins


# Ignore `module level import not at top of file` warning
# pylama: ignore=E402

# API Resources imports
from api.resources import blueprint

# Register the blueprint
factory.register(blueprint)


__all__ = ['Factory', 'HelloWorld']
