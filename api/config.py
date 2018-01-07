"""Application Configuration."""
import os

# Disable pylint "Too few public methods" warnings
# pylint: disable=R0903


class Config(object):
    """Parent configuration class."""

    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')

    TITLE = "Flask API skeleton"
    VERSION = "0.1.0"
    DESCRIPTION = "An API Skeleton."


class DevelopmentConfig(Config):
    """Configurations for Development."""

    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing."""

    TESTING = True
    DEBUG = True


class StagingConfig(Config):
    """Configurations for Staging."""

    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""

    DEBUG = False
    TESTING = False


# Disable pylint "Invalid constant name" warnings
# pylint: disable=C0103

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
