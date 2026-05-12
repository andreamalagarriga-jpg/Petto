import pandas as pd

from data.followups_repository import fetch_all_followups


def export_followups_csv():
    """
    Exporta CSV a /tmp.

    Returns:
        str
    """

    try:
        followups = fetch_all_followups()

        dataframe = pd.DataFrame(followups)

        file_path = "/tmp/followups.csv"

        dataframe.to_csv(
            file_path,
            index=False
        )

        return file_path

    except Exception as error:
        raise RuntimeError(
            f"Error exportando CSV: {error}"
        )
