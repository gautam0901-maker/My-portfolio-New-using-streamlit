import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def render_contact_section():
    st.header("Contact")
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    if st.button("Send"):
        if name and email and message:
            try:
                scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
                import os
                json_key_path = "mymessage-415909-c7d7c7997d1c.json"
                creds = ServiceAccountCredentials.from_json_keyfile_name(json_key_path, scope)
                client = gspread.authorize(creds)

                # Open the sheet by its name or URL
                sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1Mj26ELNSTp1wjv3b9w7fl7JTB0t2gOo2JMVxfEufTnQ/edit?usp=sharing").sheet1

                sheet.append_row([name, email, message, str(datetime.now())])
                st.success("Message saved to Google Sheet successfully!")
            except Exception as e:
                st.error(f"Failed to save message: {e}")
        else:
            st.warning("Please fill in all fields.")