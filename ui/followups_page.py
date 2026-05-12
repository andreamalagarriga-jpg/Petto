import streamlit as st

from config import (
    MIN_ADAPTATION_SCORE,
    MAX_ADAPTATION_SCORE
)

from data.followups_repository import (
    create_followup,
    fetch_all_followups
)

from logic.risk_logic import calculate_risk_label


def render_followups_page():
    """
    Renderiza seguimientos.
    """

    st.subheader("Seguimiento")

    with st.form("followup_form"):
        pet_name = st.text_input("Mascota")
        adopter_name = st.text_input("Adoptante")

        adaptation_score = st.slider(
            "Nivel adaptación",
            MIN_ADAPTATION_SCORE,
            MAX_ADAPTATION_SCORE,
            5
        )

        notes = st.text_area("Notas")

        submitted = st.form_submit_button("Guardar")

        if submitted:
            create_followup(
                pet_name,
                adopter_name,
                adaptation_score,
                notes
            )

            st.success("Seguimiento guardado")

    followups = fetch_all_followups()

    for followup in followups:
        risk = calculate_risk_label(
            followup["adaptation_score"]
        )

        st.card = st.container()

        with st.card:
            st.write(
                f"🐾 {followup['pet_name']}"
            )

            st.caption(
                f"Riesgo: {risk}"
            )
