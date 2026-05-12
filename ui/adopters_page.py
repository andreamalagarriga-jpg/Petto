import streamlit as st

from data.adopters_repository import create_adopter
from logic.validation_logic import validate_required_text


def render_adopters_page():
    """
    Renderiza página adoptantes.
    """

    st.subheader("Registrar Adoptante")

    st.write(
        "Crea perfiles claros para mejorar acompañamiento y seguimiento."
    )

    with st.form("adopters_form"):
        full_name = st.text_input(
            "Nombre completo",
            help="Nombre de la persona responsable."
        )

        city = st.text_input(
            "Ciudad",
            help="Ciudad donde vivirá la mascota."
        )

        experience = st.selectbox(
            "Experiencia previa",
            [
                "Primerizo",
                "Intermedio",
                "Experto"
            ]
        )

        submitted = st.form_submit_button("Guardar adoptante")

        if submitted:
            valid_name, error_name = validate_required_text(
                full_name,
                "Nombre"
            )

            valid_city, error_city = validate_required_text(
                city,
                "Ciudad"
            )

            if not valid_name:
                st.error(error_name)
                return

            if not valid_city:
                st.error(error_city)
                return

            with st.spinner("Guardando adoptante..."):
                success, message = create_adopter(
                    full_name,
                    city,
                    experience
                )

            if success:
                st.success(message)
                st.toast("Perfil creado correctamente.")
            else:
                st.error(message)
