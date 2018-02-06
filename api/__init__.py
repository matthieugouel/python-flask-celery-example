"""Initialization module of the package."""
# API Factory imports
from api.factory import Factory

# API configuration imports
from api.config import Config

# Version handling
import pkg_resources

try:
    # If the app is packaged
    # Get the version of the setup package
    __version__ = pkg_resources.get_distribution('api').version
except pkg_resources.DistributionNotFound:  # pragma: no cover
    # If app is not used as a package
    # Hardcode the version from the configuration file
    __version__ = Config.VERSION


# Instantiation of the factory
factory = Factory()

# Enable flask instance
factory.set_flask()

# Enable of the desired plugins
factory.set_celery()

# API Resources imports
from api.resources import blueprint  # noqa: E402

# Register the blueprint
factory.register(blueprint)


__all__ = ['Factory', 'HelloWorld', 'ByeWorld']
