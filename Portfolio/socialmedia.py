import streamlit as st

def render_social_media():
    st.markdown("## 🌐 Connect with Me")
    st.markdown("Feel free to reach out or follow me on these platforms:")

    card_style = """
    <style>
    .social-grid {
        display: grid;
        grid-template-columns: repeat(4, 160px);
        gap: 50px;
        max-width: 100%;
        margin: 50px auto;
        overflow-x: auto;
        justify-content: center;
    }
    .flip-card {
        background-color: transparent;
        width: 200px;
        height: 260px;
        perspective: 1000px;
        border-radius: 12px;
        overflow: hidden;
    }
    .flip-card-inner {
        position: relative;
        width: 95%;
        height: 95%;
        margin: auto;
        text-align: center;
        transition: transform 0.6s;
        transform-style: preserve-3d;
    }
    .flip-card:hover .flip-card-inner {
        transform: rotateY(180deg);
    }
    .flip-card-front, .flip-card-back {
        position: absolute;
        width: 100%;
        height: 100%;
        padding: 20px;
        backface-visibility: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.15);
        font-weight: bold;
        font-size: 16px;
    }
    .flip-card-front {
        background-color: #e0f0ff;
        color: #003366;
    }
    .flip-card-back {
        background-color: #007acc;
        color: white;
        transform: rotateY(180deg);
    }
    .flip-card-back img {
        width: 130px;
        height: 130px;
    }
    </style>
    """

    st.markdown(card_style, unsafe_allow_html=True)

    st.markdown('''
    <div class="social-grid">
      <div class="flip-card">
        <div class="flip-card-inner">
          <div class="flip-card-front" style="background-color: #e0f0ff; color: #003366;">GitHub</div>
          <div class="flip-card-back">
            <div>
              <img src="https://api.qrserver.com/v1/create-qr-code/?data=https://github.com/gautam0901-maker&amp;size=120x120" alt="GitHub QR">
              <br><br>
              <a href="https://github.com/gautam0901-maker" target="_blank" style="padding: 8px 16px; background-color: white; color: #007acc; border-radius: 8px; text-decoration: none;">Visit</a>
            </div>
          </div>
        </div>
      </div>

      <div class="flip-card">
        <div class="flip-card-inner">
          <div class="flip-card-front" style="background-color: #e0f0ff; color: #003366;">LinkedIn</div>
          <div class="flip-card-back">
            <div>
              <img src="https://api.qrserver.com/v1/create-qr-code/?data=https://www.linkedin.com/in/gautam-ramesh-8b8011214?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app&amp;size=120x120" alt="LinkedIn QR">
              <br><br>
              <a href="https://www.linkedin.com/in/gautam-ramesh-8b8011214?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app" target="_blank" style="padding: 8px 16px; background-color: white; color: #007acc; border-radius: 8px; text-decoration: none;">Visit</a>
            </div>
          </div>
        </div>
      </div>

      <div class="flip-card">
        <div class="flip-card-inner">
          <div class="flip-card-front" style="background-color: #e0f0ff; color: #003366;">Discord</div>
          <div class="flip-card-back">
            <div>
              <img src="https://api.qrserver.com/v1/create-qr-code/?data=https://discordapp.com/users/_awaken0901&amp;size=120x120" alt="Discord QR">
              <br><br>
              <a href="https://discordapp.com/users/_awaken0901" target="_blank" style="padding: 8px 16px; background-color: white; color: #007acc; border-radius: 8px; text-decoration: none;">Visit</a>
            </div>
          </div>
        </div>
      </div>

      <div class="flip-card">
        <div class="flip-card-inner">
          <div class="flip-card-front" style="background-color: #e0f0ff; color: #003366;">Gmail</div>
          <div class="flip-card-back">
            <div>
              <img src="https://api.qrserver.com/v1/create-qr-code/?data=mailto:gaudeep0901@gmail.com&amp;size=120x120" alt="Gmail QR">
              <br><br>
              <a href="mailto:gaudeep0901@gmail.com" style="padding: 8px 16px; background-color: white; color: #007acc; border-radius: 8px; text-decoration: none;">Send Email</a>
            </div>
          </div>
        </div>
      </div>

      <div class="flip-card">
        <div class="flip-card-inner">
          <div class="flip-card-front" style="background-color: #e0f0ff; color: #003366;">Medium</div>
          <div class="flip-card-back">
            <div>
              <img src="https://api.qrserver.com/v1/create-qr-code/?data=https://medium.com/@gaudeep0901&amp;size=120x120" alt="Medium QR">
              <br><br>
              <a href="https://medium.com/@gaudeep0901" target="_blank" style="padding: 8px 16px; background-color: white; color: #007acc; border-radius: 8px; text-decoration: none;">Visit</a>
            </div>
          </div>
        </div>
      </div>
    </div>
    ''', unsafe_allow_html=True)
