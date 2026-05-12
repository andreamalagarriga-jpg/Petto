import streamlit as st
import pandas as pd
from database import (
    init_db,
    add_pet,
    add_adopter,
    create_followup,
    get_pets,
    get_adopters,
    get_followups,
)
from utils import risk_label

st.set_page_config(
    page_title="Petto",
    page_icon="🐾",
    layout="wide"
)

init_db()

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Petto")
st.caption("Seguimiento post-adopción para refugios y adoptantes")

menu = st.sidebar.radio(
    "Navegación",
    [
        "Dashboard",
        "Nueva Mascota",
        "Nuevo Adoptante",
        "Seguimiento",
    ]
)

if menu == "Dashboard":
    st.subheader("Estado General")

    pets = get_pets()
    adopters = get_adopters()
    followups = get_followups()

    c1, c2, c3 = st.columns(3)

    c1.metric("Mascotas", len(pets))
    c2.metric("Adoptantes", len(adopters))
    c3.metric("Seguimientos", len(followups))

    st.divider()

    st.subheader("Mascotas en seguimiento")

    if len(pets) > 0:
        df = pd.DataFrame(pets)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("Todavía no hay mascotas registradas.")

    st.divider()

    st.subheader("Riesgo de devolución")

    if len(followups) > 0:
        followup_df = pd.DataFrame(followups)
        followup_df["risk"] = followup_df["adaptation_score"].apply(risk_label)
        st.dataframe(followup_df, use_container_width=True)
    else:
        st.warning("No existen seguimientos todavía.")

elif menu == "Nueva Mascota":
    st.subheader("Registrar Mascota")

    with st.form("pet_form"):
        name = st.text_input("Nombre")
        species = st.selectbox("Especie", ["Perro", "Gato"])
        age = st.number_input("Edad", min_value=0, max_value=30)
        notes = st.text_area("Notas")

        submitted = st.form_submit_button("Guardar")

        if submitted:
            add_pet(name, species, age, notes)
        st.dataframe(df, use_container_width=True)
