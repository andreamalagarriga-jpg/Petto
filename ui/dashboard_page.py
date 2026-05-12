import pandas as pd
import streamlit as st

from data.pets_repository import fetch_all_pets
from data.adopters_repository import fetch_all_adopters
from data.followups_repository import fetch_all_followups
from logic.risk_logic import calculate_risk_label


def render_dashboard_page():
    """
    Renderiza dashboard principal.
    """

    pets = fetch_all_pets()
    adopters = fetch_all_adopters()
    followups = fetch_all_followups()

    c1, c2, c3 = st.columns(3)

    c1.metric("Mascotas", len(pets))
    c2.metric("Adoptantes", len(adopters))
    c3.metric("Seguimientos", len(followups))

    st.divider()

    if followups:
        dataframe = pd.DataFrame(followups)

        dataframe["risk"] = dataframe[
            "adaptation_score"
        ].apply(calculate_risk_label)

        st.dataframe(
            dataframe,
            use_container_width=True
        )
