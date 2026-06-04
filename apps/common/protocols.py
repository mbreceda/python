import io
from typing import Protocol


class Readable(Protocol):
    """Structural interface for any object that can fetch content from a URL."""

    def read_url(self, decode: str = "utf-8") -> io.StringIO: ...
