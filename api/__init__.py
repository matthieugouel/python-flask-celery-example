"""Initialization module of the package."""
# Disable pylint "Unable to import" warnings
# pylint: disable=E0401

# Flask based imports
from flask import Flask

# API configuration imports
from api.config import Config, config

# API Resources imports
from api.resources import api


# Version handling
import pkg_resources

try:
    # If the app is packaged
    # Get the version of the setup package
    __version__ = pkg_resources.get_distribution('api').version
except pkg_resources.DistributionNotFound:
    # If app is not used as a package
    # Hardcoded configuration version
    __version__ = Config.VERSION


# Disable pylint "Invalid constant name" warnings
# pylint: disable=C0103

def create_app(config_name, **kwargs):
    """Entrypoint of the application."""
    # App instanctiation
    app = Flask(__name__, **kwargs)

    # Configuration options
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.py')

    # Swagger documentation options
    app.config.SWAGGER_UI_DOC_EXPANSION = 'list'
    app.config.SWAGGER_UI_JSONEDITOR = True

    # API registration
    api.init_app(app)

    return app


__all__ = ('HelloWorld')
