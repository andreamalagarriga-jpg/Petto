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

            p, label {
                color: #1A1A1A;
            }

            .stButton button {
                background-color: #F96167;
                color: white;
                border-radius: 10px;
                border: none;
                padding: 0.5rem 1rem;
            }

            .stButton button:hover {
                background-color: #e14f55;
                color: white;
            }

            [data-testid="stMetric"] {
                background: white;
                padding: 1rem;
                border-radius: 12px;
                border: 1px solid #f0f0f0;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
