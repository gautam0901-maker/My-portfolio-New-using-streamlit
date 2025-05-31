import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import aboutme
import socialmedia

try:
    from streamlit_js_eval import streamlit_js_eval, get_geolocation
except ModuleNotFoundError:
    import os
    os.system("pip install streamlit-js-eval")
    from streamlit_js_eval import streamlit_js_eval, get_geolocation


# App config
st.set_page_config(page_title="Gautam Ramesh | Portfolio", layout="wide")
st.balloons()

st.markdown(
    """
    <style>
    /* Add bottom padding to the main Streamlit content container */
    .reportview-container .main .block-container {
        padding-bottom: 120px;
    }
    body {
        background: linear-gradient(135deg, #f0f4f8 0%, #d9e2ec 100%);
        background-attachment: fixed;
        /* Optional subtle texture */
        /* background-image: url('https://www.transparenttextures.com/patterns/quiet-sunshine.png'); */
        /* background-repeat: repeat; */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar
with st.sidebar:
    st.markdown(
        """
        <style>
            .sidebar-container {
                padding: 15px;
                margin: 20px;
                border-radius: 30px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                width: 220px;
                margin-left: auto;
                margin-right: auto;
            }
            .sidebar-img {
                display: block;
                margin-left: auto;
                margin-right: auto;
                border-radius: 50%;
                border: 2px solid #4facfe;
            }
            .sidebar-title {
                text-align: center;
                font-size: 22px;
                font-weight: bold;
                margin-top: 10px;
                animation: fadeIn 1.2s ease-in-out;
            }
            .sidebar-subtitle {
                text-align: center;
                font-size: 16px;
                color: #888;
                animation: fadeIn 1.2s ease-in-out;
            }
            .contact-info {
                font-size: 15px;
                line-height: 1.6;
                padding-left: 10px;
            }
            .social-icons {
                margin: 0 10px;
                text-decoration: none;
                font-size: 20px;
                animation: fadeIn 2s ease-in;
            }
            .download-btn {
                display: flex;
                justify-content: center;
                margin-top: 15px;
            }
            @keyframes fadeIn {
                from {{ opacity: 0; transform: translateY(10px); }}
                to {{ opacity: 1; transform: translateY(0); }}
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="display: flex; justify-content: center;">
          <div class="sidebar-container">
              <img src="https://avatars.githubusercontent.com/u/118598003?v=4" width="120" class="sidebar-img" />
              <div class="sidebar-title">Gautam Ramesh</div>
              <div class="sidebar-subtitle">Software Engineer</div>
              <div class="sidebar-subtitle">BI Developer | Data Analyst</div>
              <hr>
              <div class="contact-info">
              📍 <strong>Location:</strong> Emden, Germany<br>
              📞 <strong>Phone:</strong> +49 155 10820227<br>
              📧 <strong>Email:</strong> gaudeep3309@gmail.com<br>
              </div>
              <hr>
              🧭 <strong>Mission:</strong> Empowering businesses with intelligent data solutions.
              <hr>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("""
    <style>
        .pill-tabs {
            display: flex;
            justify-content: center;
            margin: 10px 0 5px 0;
            flex-wrap: wrap;
            column-gap: -8px;
        }
        .pill-tab {
            background-color: #f0f2f6;
            color: #333;
            border: none;
            border-radius: 999px;
            padding: 6px 12px;
            margin: 0 0 0 0;
            font-size: 15px;
            cursor: pointer;
            transition: background-color 0.3s, color 0.3s;
            text-decoration: none;
            display: inline-block;
        }
        .pill-tab.active {
            background: linear-gradient(to right, #4facfe, #00f2fe);
            color: white;
            font-weight: bold;
        }
        html, body, .main {
            background-color: transparent !important;
        }
    </style>
""", unsafe_allow_html=True)


# Welcome message at the top of the tab section
st.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <h2 style="font-weight: bold; color: #4facfe; font-size: 30px;">Welcome to My Portfolio</h2>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .stTabs [data-baseweb="tab-list"] {
            justify-content: center;
        }
    </style>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["About Me", "Contact", "Gautam's Personal AI", "Social Media"])

with tab1:
    aboutme.render_about_section()

with tab2:
    import Contact
    Contact.render_contact_section()

with tab3:
    import AIChatAssistant
    AIChatAssistant.render_chat_assistant()

with tab4:
    socialmedia.render_social_media()