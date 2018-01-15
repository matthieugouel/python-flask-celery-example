"""Initialization module of Resources."""
# Flask based imports
from flask import Blueprint
from flask_restplus import Api

# Api based imports
from api.config import Config

# Resources based imports
from api.resources.main import api as main

blueprint = Blueprint('api', __name__, url_prefix='/api')

# API instantiation
api = Api(blueprint,
          title=Config.TITLE,
          version=Config.VERSION,
          description=Config.DESCRIPTION)

# Namespaces registration
api.add_namespace(main, path='')
