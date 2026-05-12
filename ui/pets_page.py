import streamlit as st

from data.pets_repository import create_pet
from logic.validation_logic import validate_required_text


def render_pets_page():
    """
    Renderiza registro mascotas.
    """

    st.subheader("Registrar Mascota")

    with st.form("pets_form"):
        name = st.text_input("Nombre")
        species = st.selectbox(
            "Especie",
            ["Perro", "Gato"]
        )

        age = st.number_input(
            "Edad",
            min_value=0,
            max_value=30
        )

        notes = st.text_area("Notas")

        submitted = st.form_submit_button("Guardar")

        if submitted:
            valid, error = validate_required_text(
                name,
                "Nombre"
            )

            if not valid:
                st.error(error)
                return

            create_pet(
                name,
                species,
                age,
                notes
            )

            st.success("Mascota registrada")
