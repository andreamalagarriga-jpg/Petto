import pandas as pd
import streamlit as st

from data.adopters_repository import fetch_all_adopters
from data.followups_repository import fetch_all_followups
from data.pets_repository import fetch_all_pets
from logic.risk_logic import calculate_risk_label


def render_dashboard_page():
    """
    Renderiza dashboard principal.
    """

    pets = fetch_all_pets()
    adopters = fetch_all_adopters()
    followups = fetch_all_followups()

    st.subheader("Dashboard General")

    st.write(
        "Visualiza rápidamente casos que necesitan atención y seguimiento."
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Mascotas registradas",
        len(pets)
    )

    c2.metric(
        "Adoptantes activos",
        len(adopters)
    )

    c3.metric(
        "Seguimientos realizados",
        len(followups)
    )

    st.divider()

    if not followups:
        st.info(
            "Aún no hay seguimientos para analizar."
        )
        return

    dataframe = pd.DataFrame(followups)

    dataframe["Riesgo"] = dataframe[
        "adaptation_score"
    ].apply(calculate_risk_label)

    dataframe = dataframe.rename(
        columns={
            "pet_name": "Mascota",
            "adopter_name": "Adoptante",
            "adaptation_score": "Adaptación",
            "notes": "Notas",
        }
    )

    st.dataframe(
        dataframe,
        use_container_width=True
    )
