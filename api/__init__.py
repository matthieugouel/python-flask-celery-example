"""Initialization module of the package."""
# Disable pylint "Unable to import ..." warnings
# pylint: disable=E0401
from flask import Flask, Blueprint
from flask_restful import Api

from api.resources.main import HelloWorld

# Package version handling
import pkg_resources

try:
    __version__ = pkg_resources.get_distribution('api').version
except pkg_resources.DistributionNotFound:
    __version__ = "Not installed"

# Disable pylint "Invalid constatnt name" warnings
# pylint: disable=C0103

# API Instanciation
app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(HelloWorld, '/')
app.register_blueprint(api_bp, url_prefix='/api')

__all__ = ['HelloWorld']
