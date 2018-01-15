"""Main entrypint of the application."""
import os

# Api based imports
from api import create_app

# Try to get the environment from an environment variable
environment = os.getenv('APP_ENVIRONMENT')

# Force the environment to default if not already set
if not environment:
    environment = 'default'

# Create flask instance
app = create_app(environment)

if __name__ == '__main__':
    # Actually run the application
    app.run()
