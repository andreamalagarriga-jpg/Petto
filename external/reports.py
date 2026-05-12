import pandas as pd

from data.followups_repository import fetch_all_followups


def export_followups_csv():
    """
    Exporta CSV temporal.
    """

    try:
        followups = fetch_all_followups()

        if not followups:
            return False, "No existen seguimientos para exportar."

        dataframe = pd.DataFrame(followups)

        file_path = "/tmp/petto_followups.csv"

        dataframe.to_csv(
            file_path,
            index=False
        )

        return True, file_path

    except Exception as error:
        return False, f"Error exportando CSV: {error}"
