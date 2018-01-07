"""Initialization module of Resources."""
# Disable pylint "Unable to import" warnings
# pylint: disable=E0401

# Flask based imports
from flask import Blueprint
from flask_restplus import Api

# Resources based imports
from api.resources.main import api as main

from api.config import Config


# Disable pylint "Invalid constant name" warnings
# pylint: disable=C0103

blueprint = Blueprint('api', __name__, url_prefix='/api')

# API instanciation
api = Api(blueprint,
          title=Config.TITLE,
          version=Config.VERSION,
          description=Config.DESCRIPTION)

# Namespaces registration
api.add_namespace(main, path='')
