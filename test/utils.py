"""Utils helpers."""
import json
from flask import Response
from werkzeug.utils import cached_property


class JSONResponse(Response):
    """A Response class with ``.json`` property."""

    @cached_property
    def json(self):
        """Json response method."""
        return json.loads(self.get_data(as_text=True))
