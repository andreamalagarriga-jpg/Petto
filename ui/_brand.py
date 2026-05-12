import streamlit as st


def inject_brand():
    """
    Inyecta sistema visual Petto.
    """

    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Roboto+Mono:wght@500&display=swap');

        :root {
            --primary: #0061EF;
            --secondary: #FF6500;
            --accent: #1CA059;

            --bg: #FAFAFA;
            --surface: #FFFFFF;
            --border: #E8E8E8;
            --text: #1F2937;
            --muted: #6B7280;

            --radius-sm: 4px;
            --radius-md: 8px;
            --radius-lg: 16px;

            --shadow-sm: 0 1px 2px rgba(0,0,0,0.04);
            --shadow-md: 0 8px 24px rgba(0,0,0,0.08);
            --shadow-lg: 0 20px 40px rgba(0,0,0,0.12);
        }

        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
            color: var(--text);
        }

        .stApp {
            background: var(--bg);
        }

        section.main > div {
            max-width: 1200px;
            padding-top: 2rem;
        }

        h1, h2, h3 {
            font-family: 'Poppins', sans-serif;
            font-weight: 700;
            letter-spacing: -0.03em;
            color: var(--text);
        }

        h1 {
            font-size: 3rem;
        }

        h2 {
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }

        p, label, span {
            color: var(--text);
            font-size: 0.96rem;
        }

        .stSidebar {
            background: #FFFFFF;
            border-right: 1px solid var(--border);
        }

        .stSidebar h1,
        .stSidebar h2,
        .stSidebar label {
            color: var(--text);
        }

        .stButton button {
            background: var(--primary);
            color: white;
            border: none;
            border-radius: var(--radius-md);
            padding: 0.75rem 1.2rem;
            font-weight: 600;
            transition: 0.2s ease;
            box-shadow: var(--shadow-sm);
        }

        .stButton button:hover {
            background: #0052CA;
            transform: translateY(-1px);
            box-shadow: var(--shadow-md);
        }

        .stDownloadButton button {
            background: var(--secondary);
            color: white;
            border-radius: var(--radius-md);
            border: none;
            padding: 0.75rem 1.2rem;
            font-weight: 600;
        }

        .stTextInput input,
        .stNumberInput input,
        .stTextArea textarea,
        .stSelectbox div[data-baseweb="select"] {
            border-radius: var(--radius-md);
            border: 1px solid var(--border);
            background: var(--surface);
            padding: 0.75rem;
            font-size: 0.95rem;
        }

        .stTextInput input:focus,
        .stTextArea textarea:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 1px var(--primary);
        }

        .stForm {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 1.5rem;
            box-shadow: var(--shadow-sm);
        }

        [data-testid="stMetric"] {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 1rem;
            box-shadow: var(--shadow-sm);
        }

        [data-testid="stMetricLabel"] {
            color: var(--muted);
            font-weight: 500;
        }

        [data-testid="stMetricValue"] {
            color: var(--text);
            font-weight: 700;
        }

        .stAlert {
            border-radius: var(--radius-md);
        }

        .stProgress > div > div {
            background-color: var(--accent);
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 4rem;
        }

        hr {
            border: none;
            border-top: 1px solid var(--border);
            margin: 2rem 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
