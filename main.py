from apps.table_viewer import TableViewer


def main():
    url = "https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)"
    viewer = TableViewer(url)

    df = viewer.get_dataframe(index=0)
    viewer.display_table(df, title="List of The Simpsons episodes (seasons 1–20)")


if __name__ == "__main__":
    main()
