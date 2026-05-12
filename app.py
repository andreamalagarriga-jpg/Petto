import streamlit as st

from config import APP_TITLE, APP_DESCRIPTION
from data.migrations import initialize_database
from ui.dashboard_page import render_dashboard_page
from ui.pets_page import render_pets_page
from ui.adopters_page import render_adopters_page
from ui.followups_page import render_followups_page
from ui._brand import inject_brand_styles

st.set_page_config(
    page_title=APP_TITLE,
    layout="wide"
)

initialize_database()
inject_brand_styles()

st.title(APP_TITLE)
st.caption(APP_DESCRIPTION)

page = st.sidebar.radio(
    "Navegación",
    [
        "Dashboard",
        "Mascotas",
        "Adoptantes",
        "Seguimientos",
    ]
)

if page == "Dashboard":
    render_dashboard_page()

elif page == "Mascotas":
    render_pets_page()

elif page == "Adoptantes":
    render_adopters_page()

elif page == "Seguimientos":
    render_followups_page()
