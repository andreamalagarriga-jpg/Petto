import streamlit as st

from data.adopters_repository import create_adopter
from logic.validation_logic import validate_required_text


def render_adopters_page():
    """
    Renderiza adoptantes.
    """

    st.subheader("Registrar Adoptante")

    with st.form("adopters_form"):
        full_name = st.text_input("Nombre completo")
        city = st.text_input("Ciudad")

        experience = st.selectbox(
            "Experiencia",
            [
                "Primerizo",
                "Intermedio",
                "Experto"
            ]
        )

        submitted = st.form_submit_button("Guardar")

        if submitted:
            valid, error = validate_required_text(
                full_name,
                "Nombre"
            )

            if not valid:
                st.error(error)
                return

            create_adopter(
                full_name,
                city,
                experience
            )

            st.success("Adoptante registrado")
