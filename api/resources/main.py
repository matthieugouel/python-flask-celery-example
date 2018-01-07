"""Entrypoint of the main API Resources."""
# Disable pylint "Unable to import" warnings
# pylint: disable=E0401
from flask_restplus import Resource, Namespace


# Disable pylint "Invalid constant name" warnings
# pylint: disable=C0103

api = Namespace('main', description='Main API namespace.')


# Disable pylint "Too few public methods" warnings
# pylint: disable=R0903
# Disable pylint "Method could be a function" warnings
# pylint: disable=R0201

@api.route('/hello/<name>')
@api.doc(params={'name': 'The name of the person to return hello.'})
class HelloWorld(Resource):
    """HelloWorld resource class."""

    def get(self, name):
        """Get method."""
        return {'hello': name}
