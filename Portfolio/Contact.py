import streamlit as st
import json
import os
from datetime import datetime
from uuid import uuid4

def render_contact_section():
    st.markdown("## 📬 Contact")

    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    if st.button("Send"):
        if not name or not email or not message:
            st.warning("Please fill in all fields.")
            return

        data = {
            "id": str(uuid4()),
            "timestamp": datetime.now().isoformat(),
            "name": name,
            "email": email,
            "message": message
        }

        try:
            # Ensure messages folder exists
            os.makedirs("messages", exist_ok=True)

            # Generate filename
            filename = f"messages/message-{datetime.now().strftime('%Y%m%d%H%M%S')}.json"

            # Save JSON file
            with open(filename, "w") as f:
                json.dump(data, f, indent=4)

            st.success("✅ Message sent successfully!")

        except Exception as e:
            st.error(f"❌ Failed to save message: {e}")
