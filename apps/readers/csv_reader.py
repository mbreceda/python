import pandas as pd

from apps.protocols import Readable


class CsvReader:
    def __init__(self, request: Readable) -> None:
        self.request = request

    def get_dataframe(self) -> pd.DataFrame:
        """Fetch a CSV from the URL and return it as a DataFrame.

        Uses urllib to follow redirects (e.g. http → https) and set a
        browser User-Agent, then passes the content as StringIO to
        pd.read_csv — avoiding the ParserError caused by reading an
        HTML redirect page as if it were CSV.
        """
        return pd.read_csv(self.request.read_url())
