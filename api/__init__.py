"""Initialization module of the package."""
# Disable pylint "Unable to import ..." warnings
# pylint: disable=E0401

# Flask based imports
from flask import Flask, Blueprint
from flask_restful import Api

# API Configuraion imports
from api.config import api_config

# API Resources imports
from api.resources.main import HelloWorld

# Package version handling
import pkg_resources

try:
    __version__ = pkg_resources.get_distribution('api').version
except pkg_resources.DistributionNotFound:
    __version__ = "Not installed"


# Disable pylint "Invalid constatnt name" warnings
# pylint: disable=C0103

# API creation
def create_app(config_name):
    """API Creation."""
    # App instanctiation
    app = Flask(__name__)

    # Confiuration options
    app.config.from_object(api_config[config_name])
    app.config.from_pyfile('config.py')

    # API instanciation
    api_bp = Blueprint('api', __name__)
    api = Api(api_bp)

    # Resources registration
    api.add_resource(HelloWorld, '/')
    app.register_blueprint(api_bp, url_prefix='/api')

    return app


__all__ = ['HelloWorld']
