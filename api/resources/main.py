"""Entrypoint of the main API Resources."""
# Flask based imports
from flask_restplus import Resource, Namespace

# Empty name is required to have the desired url path
api = Namespace(name='', description='Main API namespace.')


@api.route('/hello/<name>')
@api.doc(params={'name': 'The name of the person to return hello.'})
class HelloWorld(Resource):
    """HelloWorld resource class."""

    def get(self, name):
        """Get method."""
        return {'hello': name}
