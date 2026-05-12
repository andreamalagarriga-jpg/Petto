import streamlit as st

from data.pets_repository import create_pet
from logic.validation_logic import (
    validate_positive_number,
    validate_required_text,
)


def render_pets_page():
    """
    Renderiza página mascotas.
    """

    st.subheader("Registrar Mascota")

    st.write(
        "Centraliza la información de cada mascota para reducir pérdidas de seguimiento."
    )

    with st.form("pets_form"):
        name = st.text_input(
            "Nombre",
            help="Usa el nombre actual de la mascota."
        )

        species = st.selectbox(
            "Especie",
            ["Perro", "Gato"]
        )

        age = st.number_input(
            "Edad",
            min_value=0,
            max_value=30
        )

        notes = st.text_area(
            "Notas",
            placeholder="Comportamiento, salud o adaptación."
        )

        submitted = st.form_submit_button("Guardar mascota")

        if submitted:
            valid_name, error_name = validate_required_text(
                name,
                "Nombre"
            )

            if not valid_name:
                st.error(error_name)
                return

            valid_age, error_age = validate_positive_number(
                age,
                "Edad"
            )

            if not valid_age:
                st.error(error_age)
                return

            with st.spinner("Guardando mascota..."):
                success, message = create_pet(
                    name,
                    species,
                    age,
                    notes
                )

            if success:
                st.success(message)
                st.toast("Mascota lista para seguimiento.")
            else:
                st.error(message)
