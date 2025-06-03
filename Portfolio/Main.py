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

# Show loading animation once
if "visited" not in st.session_state:
    st.session_state.visited = True
    st.markdown("""
        <style>
            .loader {
                border: 8px solid #f3f3f3;
                border-top: 8px solid #3498db;
                border-radius: 50%;
                width: 80px;
                height: 80px;
                animation: spin 1.2s linear infinite;
                margin: auto;
                margin-top: 200px;
            }
            .loading-text {
                text-align: center;
                font-size: 18px;
                color: #555;
                margin-top: 20px;
                font-weight: 500;
            }
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
        </style>
        <div class="loader"></div>
        <div class="loading-text">Loading Gautam's Portfolio...</div>
    """, unsafe_allow_html=True)
    st.stop()

st.balloons()

# Background styling
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #f0f4f8 0%, #d9e2ec 100%);
            background-attachment: fixed;
        }
        .stTabs [data-baseweb="tab-list"] {
            justify-content: center;
        }
        .fade-in {
            animation: fadeIn 1s ease-in;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(15px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
        <div style="padding: 15px; margin: 20px; border-radius: 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); text-align: center;">
            <img src="https://avatars.githubusercontent.com/u/118598003?v=4" width="120" style="border-radius: 50%; border: 2px solid #4facfe;" />
            <div style="font-size: 22px; font-weight: bold; margin-top: 10px;">Gautam Ramesh</div>
            <div style="font-size: 16px; color: #888;">Software Engineer</div>
            <div style="font-size: 16px; color: #888;">BI Developer | Data Analyst</div>
            <hr>
            <div style="font-size: 14px; text-align: left;">
                📍 <strong>Location:</strong> Emden, Germany<br>
                📞 <strong>Phone:</strong> +49 155 10820227<br>
                📧 <strong>Email:</strong> gaudeep3309@gmail.com<br>
            </div>
            <hr>
            🧭 <strong>Mission:</strong> Empowering businesses with intelligent data solutions.
            <hr>
        </div>
    """, unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="fade-in" style="text-align: center; margin-top: 20px;">
        <h2 style="font-weight: bold; color: #4facfe;">Welcome to My Portfolio</h2>
    </div>
""", unsafe_allow_html=True)

# Tabs
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
