"""Initialization module of the package."""
# Flask based imports
from flask import Flask

# API configuration imports
from api.config import Config, config

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


def create_app(environment, **kwargs):
    """Setup of the application."""
    # App instantiation
    app = Flask(__name__, **kwargs)

    # App configuration
    app.config.from_object(config[environment])
    app.config.from_pyfile('config.py')

    # Swagger documentation
    app.config.SWAGGER_UI_DOC_EXPANSION = 'list'
    app.config.SWAGGER_UI_JSONEDITOR = True

    # API Resources imports
    from api.resources import blueprint

    # API registration
    app.register_blueprint(blueprint)

    return app


__all__ = ('HelloWorld')
