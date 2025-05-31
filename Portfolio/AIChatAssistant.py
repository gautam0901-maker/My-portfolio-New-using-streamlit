import streamlit as st
import google.generativeai as genai
import os

# Set your Gemini API key directly in code
GEMINI_API_KEY = "AIzaSyAr7V8xbKjceqP0tf0X_OdEL8bg1ON6qVk"
genai.configure(api_key=GEMINI_API_KEY)

def get_gemini_response(query):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        chat = model.start_chat()
        resume_context = """
  Gautam Ramesh is a highly motivated and diligent individual with solid work and internship experience in software development, web development, automation, and exposure to machine learning. He has worked as a Data Engineer at United Techno, a Developer Intern and Data Analyst at ZF Technologies, a Developer Trainee at Kloudlearn Technologies, and completed a software trainee role at Wipro. Additionally, he underwent Salesforce developer and admin training at Cognizant.

  Key Projects:
  - **ZF Newsletter Software**: Built using Python (Tkinter) and News API, this tool displays ZF news, upcoming events, new joiner info, patents, and a task calendar.
  - **ZF Our-Space**: An internal web portal for ZF employees to buy/sell products, built with HTML, CSS, JS, and SQL.
  - **Vehicle-to-Vehicle Communication**: A proof-of-concept project involving FM modulation for communication between cars.
  - **Power BI Dashboard**: A KPI dashboard comparing yearly performance using Itonics API and DAX.
  - **College Mobile App**: Built with Flutter and Firebase, featuring college events, admission info, and a parent-teacher forum.
  - **Weather App**: A cross-platform app using GPS and Weather API to display local weather conditions.

  Skills:
  - **Languages**: Python, C++, Java, Dart (Flutter), VBA, DAX, Lua, HTML, CSS, JS, SQL, R, LaTeX
  - **Platforms**: Salesforce (developer/admin), Power BI, Tableau, Automation Anywhere, Power Automate, Snowflake, AWS, Firebase
  - **Tools**: Excel, PowerPoint, Power Apps, Word, GitHub, JIRA

  Education:
  - **B.Tech in Information Technology**, Prince Shri Venkateshwara Padmavathi Engineering College, Chennai (2018–2022)
  - **Higher & Senior Secondary**, Modern Senior Secondary School, Chennai

  Gautam is currently pursuing a Master’s in Business Intelligence and Data Analytics in Germany, looking to expand his knowledge and apply his skills in impactful data-driven roles.

  Gautam has a deep passion for building intelligent systems and data-driven solutions. He actively engages in independent projects, such as building a professional-grade sales forecasting application with features like AI-generated insights, Google Sheets integration, drag-and-drop interface, and custom data visualizations using Flet. 

  He is a highly motivated learner, pursuing certifications such as AWS and continuously expanding his skillset in data engineering, automation, and UI/UX design. Gautam has demonstrated exceptional initiative by developing his own AI-powered portfolio assistant, integrating Google Gemini to answer questions about his qualifications, skills, and experiences.

  In addition to his technical strengths, Gautam excels at documentation and presentation, often using LaTeX and Beamer to prepare detailed manuals and technical slides. His attention to design, usability, and communication makes him a standout candidate in analytics, development, and innovation roles.

  Gautam's hobbies include playing cricket, making software, and exploring computer games. He enjoys combining creativity and logic to solve real-world problems through code.

  Certifications:
  - Completed courses in Flutter development, Python programming, and Salesforce Data Cloud.
  - Received a performance certificate from ZF Technologies for exceptional work performance during his internship.

  For more on Gautam’s projects and contributions, please visit his GitHub page: [https://github.com/gautamramesh](https://github.com/gautamramesh)

  Personal Statement:
  Gautam is a curious, self-driven learner with a passion for solving problems using data and technology. He believes in continuous improvement, learning from every experience, and making meaningful contributions wherever he works.
  """
        response = chat.send_message(f"{resume_context}\n\n{query}")
        return response.text
    except Exception as e:
        return f"An error occurred while generating the answer: {e}"

def render_chat_assistant():
    import time

    st.markdown("## 🧠 Ask Me Anything About Gautam")
    st.caption("I am the AI Assistant for Gautam. Ask your questions below.")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            placeholder = st.empty()
            for i in range(len(message["content"]) + 1):
                placeholder.markdown(message["content"][:i] + "▌")
                time.sleep(0.01)
            placeholder.markdown(message["content"])

    if query := st.chat_input("Ask me anything about Gautam..."):
        st.session_state.chat_history.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        response = get_gemini_response(query)
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            placeholder = st.empty()
            for i in range(len(response) + 1):
                placeholder.markdown(response[:i] + "▌")
                time.sleep(0.01)
            placeholder.markdown(response)
