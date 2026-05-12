import streamlit as st

from config import (
    MAX_ADAPTATION_SCORE,
    MIN_ADAPTATION_SCORE,
)

from data.followups_repository import (
    create_followup,
    fetch_all_followups,
)

from external.reports import export_followups_csv
from logic.risk_logic import calculate_risk_label
from logic.validation_logic import validate_required_text


def render_followups_page():
    """
    Renderiza seguimientos.
    """

    st.subheader("Seguimiento Post-Adopción")

    st.write(
        "Detecta problemas de adaptación antes de que terminen en devolución."
    )

    with st.form("followup_form"):
        pet_name = st.text_input(
            "Mascota",
            help="Nombre de la mascota adoptada."
        )

        adopter_name = st.text_input(
            "Adoptante",
            help="Persona responsable del hogar."
        )

        adaptation_score = st.slider(
            "Nivel de adaptación",
            MIN_ADAPTATION_SCORE,
            MAX_ADAPTATION_SCORE,
            5,
            help="1 = adaptación crítica · 10 = adaptación positiva"
        )

        notes = st.text_area(
            "Observaciones",
            placeholder="Ejemplo: ansiedad, sueño, convivencia."
        )

        submitted = st.form_submit_button(
            "Guardar seguimiento"
        )

        if submitted:
            valid_pet, error_pet = validate_required_text(
                pet_name,
                "Mascota"
            )

            valid_adopter, error_adopter = validate_required_text(
                adopter_name,
                "Adoptante"
            )

            if not valid_pet:
                st.error(error_pet)
                return

            if not valid_adopter:
                st.error(error_adopter)
                return

            with st.spinner("Guardando seguimiento..."):
                success, message = create_followup(
                    pet_name,
                    adopter_name,
                    adaptation_score,
                    notes
                )

            if success:
                st.success(message)
                st.toast("Seguimiento actualizado.")
            else:
                st.error(message)

    st.divider()

    followups = fetch_all_followups()

    if not followups:
        st.info(
            "Todavía no existen seguimientos registrados."
        )
        return

    for followup in followups:
        risk = calculate_risk_label(
            followup["adaptation_score"]
        )

        with st.container(border=True):
            st.write(
                f"🐾 {followup['pet_name']}"
            )

            st.caption(
                f"Adoptante: {followup['adopter_name']}"
            )

            st.caption(
                f"Riesgo detectado: {risk}"
            )

            st.progress(
                followup["adaptation_score"] / 10
            )

            if followup["notes"]:
                st.write(
                    followup["notes"]
                )

    st.divider()

    export_clicked = st.button(
        "Exportar reporte CSV"
    )

    if export_clicked:
        with st.spinner("Preparando reporte..."):
            success, result = export_followups_csv()

        if success:
            with open(result, "rb") as file:
                st.download_button(
                    label="Descargar reporte",
                    data=file,
                    file_name="petto_followups.csv",
                    mime="text/csv"
                )

        else:
            st.error(result)
