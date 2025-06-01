import streamlit as st
import matplotlib.pyplot as plt

def render_about_section():
    st.markdown("""
        <style>
        .animated-header {
            animation: fadeIn 2s ease-in-out;
        }
        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(-10px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        .journey-panel {
            background-color: #f0f2f6;
            color: #111111;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            animation: fadeInPanel 1.5s ease-in-out;
        }
        @media (prefers-color-scheme: dark) {
            .journey-panel {
                background-color: #1e1e1e;
                color: #f0f0f0;
            }
        }
        @keyframes fadeInPanel {
            from { opacity: 0; transform: translateX(-20px); }
            to { opacity: 1; transform: translateX(0); }
        }
        </style>
        <h2 class="animated-header">👨‍💻 About Me</h2>
    """, unsafe_allow_html=True)

    st.info("Hi, I'm **Gautam Ramesh**, a passionate developer and data engineer focused on automation and analytics.")

    st.markdown("""
        <div class="journey-panel">
        <h3>🌟 My Journey</h3>
        <ul>
          <li>🎓 Bachelor's in Information Technology</li>
          <li>💼 UnitedTechno – Snowflake, Snowpark, PySpark, Salesforce Data Cloud</li>
          <li>💼 ZF – Power BI, Python, Flutter, Tkinter, Power Automate</li>
          <li>💼 Cognizant – Salesforce Developer</li>
          <li>💼 Wipro – Front-End Web Developer</li>
          <li>🎓 Currently: Master's in Business Intelligence and Data Analytics – Germany</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🛠️ Core Skills")
    with st.expander("View My Skills"):
        st.markdown("""
        - Python | Power BI | SQL | Streamlit | Power Automate  
        - Snowflake | Snowflake Data Cloud | AWS | Firebase | PySpark | Salesforce Data Cloud | APIs | Tkinter  
        - Flutter | Web Dev (HTML, CSS, JS) | Microsoft Office Suite | Machine Learning
        """)

    st.markdown("### 📈 Progress & Interests")
    st.progress(80, text="Python Expertise")
    st.progress(80, text="Machine Learning")
    st.progress(70, text="Data Analytics & BI Tools")
    st.progress(60, text="Web Development")

    st.markdown("### 🎯 Goals")
    st.success("To build intelligent tools and deliver impactful data-driven solutions across industries.")

if __name__ == "__main__":
    render_about_section()
