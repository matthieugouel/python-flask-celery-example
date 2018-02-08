"""Entrypoint of the main API Resources."""
# Useful to simulate a long action
# from time import sleep

# Flask based imports
from flask_restplus import Resource, Namespace

# Application based imports
from api import factory

# Empty name is required to have the desired url path
api = Namespace(name='', description='Main API namespace.')

# Get the celery instance
celery = factory.celery


@api.route('/hello/<name>')
@api.doc(params={'name': 'The name of the person to return hello.'})
class HelloWorld(Resource):
    """HelloWorld resource class."""

    def get(self, name):
        """Get method."""
        return {'hello': name}


@api.route('/bye/<name>')
@api.doc(params={'name': 'The name of the person to return bye.'})
class ByeWorld(Resource):
    """ByeWorld resource class."""

    def get(self, name):
        """Get method."""
        # Asynchronous long task that we don't need to know the output
        self.asynchronous.apply_async((name,))
        return {'bye': name}

    @staticmethod
    @celery.task()
    def asynchronous(name):
        """Async long task method."""
        # sleep(5)
        return {'async': name}
