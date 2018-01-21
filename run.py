"""Main entrypint of the application."""
# Api factory import
from api import factory

# Eventually force the environment
# factory.environment = 'default'

# Get flask instance
app = factory.flask

# Get celery instance
celery = factory.celery

print(str(celery.conf))

if __name__ == '__main__':
    # Actually run the application
    app.run()
