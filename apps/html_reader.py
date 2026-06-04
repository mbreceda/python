import pandas as pd

# Rich uses Console to render text to the terminal.
from rich.console import Console

# Rich uses Table to render tables to the terminal.
from rich.table import Table

from apps.protocols import Readable


class HTMLReader:
    def __init__(self, request: Readable, console: Console | None = None) -> None:
        self._request = request
        self.console = console or Console()

    def get_dataframe(self, index: int = 0) -> pd.DataFrame:
        """Fetch all tables from the URL and return the one at the given index."""
        dataframes = pd.read_html(self._request.read_url())
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
