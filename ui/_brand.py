import streamlit as st


def inject_brand_styles():
    """
    Inyecta estilos globales.
    """

    st.markdown(
        """
        <style>
            .stApp {
                background-color: #FAF7F2;
            }

            h1, h2, h3 {
                color: #1E2761;
            }

            .stButton button {
                background-color: #F96167;
                color: white;
                border: none;
                border-radius: 8px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
