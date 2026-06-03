import io
from urllib.request import Request, urlopen

import pandas as pd

# Rich uses Console to render text to the terminal.
from rich.console import Console

# Rich uses Table to render tables to the terminal.
from rich.table import Table


class TableViewer:
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }

    def __init__(self, url: str) -> None:
        self.url = url
        self.console = Console()

    def get_dataframe(self, index: int = 0) -> pd.DataFrame:
        """Fetch all tables from the URL and return the one at the given index."""
        req = Request(self.url, headers=self.HEADERS)

        with urlopen(req) as response:
            html = io.StringIO(response.read().decode("utf-8"))
            dataframes = pd.read_html(html)

        return dataframes[index]

    @staticmethod
    def _flatten_columns(df: pd.DataFrame) -> list[str]:
        """Flatten MultiIndex columns into plain strings, or return as-is."""
        if isinstance(df.columns, pd.MultiIndex):
            return [" | ".join(str(lvl) for lvl in col).strip() for col in df.columns]
        return df.columns.astype(str).tolist()

    def display_table(self, df: pd.DataFrame, title: str) -> None:
        """Render a pandas DataFrame as a rich table in the terminal."""
        table = Table(title=title, show_header=True, header_style="bold magenta")
        columns = self._flatten_columns(df)

        # Add columns to the table
        for col in columns:
            table.add_column(col, overflow="fold")

        # Add rows to the table
        for _, row in df.iterrows():
            table.add_row(*[str(v) for v in row])

        self.console.print(table)
