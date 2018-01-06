"""Main run file."""
import os

# Api based imports
from api import create_app

# Disable pylint "Invalid constatnt name" warnings
# pylint: disable=C0103
config_name = os.getenv('APP_SETTINGS')

# If environment varialbe not present, then default configuration
if not config_name:
    config_name = 'default'

app = create_app(config_name)

if __name__ == '__main__':
    app.run()
