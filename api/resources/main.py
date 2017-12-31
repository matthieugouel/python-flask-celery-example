"""Main resources module."""
# Disable pylint "Unable to import ..." warnings
# pylint: disable=E0401
from flask_restful import Resource, reqparse

# Disable pylint "Too few public methods." warnings
# pylint: disable=R0903


class HelloWorld(Resource):
    """HelloWorld resource class."""

    def __init__(self):
        """Initialization method."""
        self.parser = reqparse.RequestParser()

        # 'foo' argument handling
        self.parser.add_argument('foo',
                                 type=str, location='json', required=True)

    def get(self):
        """Get method."""
        args = self.parser.parse_args()
        return {'hello': args['foo']}
