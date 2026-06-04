import io
from urllib.request import Request as URequest
from urllib.request import urlopen


class Request:
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }

    def __init__(self, url: str) -> None:
        self.url = url

    def read_url(self, decode: str = "utf-8") -> io.StringIO:
        req = URequest(self.url, headers=self.HEADERS)

        with urlopen(req) as response:
            return io.StringIO(response.read().decode(decode))
