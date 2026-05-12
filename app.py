import streamlit as st

from config import APP_DESCRIPTION, APP_TITLE
from data.migrations import initialize_database
from ui._brand import inject_brand_styles
from ui.adopters_page import render_adopters_page
from ui.dashboard_page import render_dashboard_page
from ui.followups_page import render_followups_page
from ui.pets_page import render_pets_page

st.set_page_config(
    page_title=APP_TITLE,
    layout="wide"
)

initialize_database()
inject_brand_styles()

st.title(APP_TITLE)
st.caption(APP_DESCRIPTION)

st.sidebar.title("Petto")

selected_page = st.sidebar.radio(
    "Ir a",
    [
        "Dashboard",
        "Mascotas",
        "Adoptantes",
        "Seguimientos",
    ]
)

if selected_page == "Dashboard":
    render_dashboard_page()

elif selected_page == "Mascotas":
    render_pets_page()

elif selected_page == "Adoptantes":
    render_adopters_page()

elif selected_page == "Seguimientos":
    render_followups_page()
