"""Utils helpers."""
# Disable pylint "Unable to import" warnings
# pylint: disable=E0401
import json
from flask import Response
from werkzeug.utils import cached_property


# Disable pylint "Too few public methods" warnings
# pylint: disable=R0903

class JSONResponse(Response):
    """A Response class with ``.json`` property."""

    @cached_property
    def json(self):
        """Json response method."""
        return json.loads(self.get_data(as_text=True))
