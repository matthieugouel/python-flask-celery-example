"""Asynchronous tests configuration."""
# Test library
import pytest

# API asynchronous tasks based imports
from api.resources.main import ByeWorld


@pytest.yield_fixture(scope='session')
def byeworld_asynchronous():
    """Fixture of ByeWorld resource."""
    return ByeWorld()
