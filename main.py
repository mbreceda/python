from apps.csv_reader import CsvReader
from apps.html_reader import HTMLReader
from apps.request import Request


def main():
    wikipedia_url = "https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)"
    viewer = HTMLReader(Request(wikipedia_url))
    df = viewer.get_dataframe(index=0)
    viewer.display_table(df, title="List of The Simpsons episodes (seasons 1–20)")

    csv_url = "https://www.football-data.co.uk/mmz4281/2122/E0.csv"
    reader = CsvReader(Request(csv_url))
    df = reader.get_dataframe()

    # Renaming column
    df.rename(
        columns={
            "FTHG": "Home Goals",
            "FTAG": "Away Goals",
        },
        inplace=True,
    )
    print(df[["Home Goals", "Away Goals"]])


if __name__ == "__main__":
    main()
