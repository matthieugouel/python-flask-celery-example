# Copyright 2017 Matthieu Gouel. All rights reserved.
#
# The contents of this file are licensed under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with the
# License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

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
