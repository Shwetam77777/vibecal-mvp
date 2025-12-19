import streamlit as st
import datetime
import pytz
import requests
from streamlit_lottie import st_lottie
import time

# --- 1. SETUP PAGE CONFIG ---
st.set_page_config(page_title="VibeCal: AI Calendar", page_icon="📅", layout="centered")

# --- 2. FUNCTION TO LOAD ANIMATIONS ---
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# --- 3. TIME & THEME LOGIC ---
IST = pytz.timezone('Asia/Kolkata')
now = datetime.datetime.now(IST)
current_hour = now.hour

# Theme Settings
if 5 <= current_hour < 12:
    period = "Morning"
    greeting = "Rise & Shine! ☀️"
    # Morning Gradient (Soft Orange)
    bg_gradient = "linear-gradient(135deg, #f5af19 0%, #f12711 100%);"
    card_color = "rgba(255, 255, 255, 0.2)"
    text_color = "#ffffff"
    lottie_url = "https://lottie.host/9355462c-6379-44d8-9477-6287950c0576/8YI5Z5vQ7e.json"
elif 12 <= current_hour < 17:
    period = "Afternoon"
    greeting = "Good Afternoon! 🌤️"
    # Afternoon Gradient (Bright Blue)
    bg_gradient = "linear-gradient(135deg, #2980B9 0%, #6DD5FA 100%);"
    card_color = "rgba(255, 255, 255, 0.25)"
    text_color = "#ffffff"
    lottie_url = "https://lottie.host/9355462c-6379-44d8-9477-6287950c0576/8YI5Z5vQ7e.json"
elif 17 <= current_hour < 20:
    period = "Evening"
    greeting = "Good Evening! 🌇"
    # Evening Gradient (Purple/Pink)
    bg_gradient = "linear-gradient(135deg, #654ea3 0%, #eaafc8 100%);"
    card_color = "rgba(0, 0, 0, 0.2)" # Darker glass for evening
    text_color = "#ffffff"
    lottie_url = "https://lottie.host/8b3f5b72-2d17-48a6-80f6-02607593c78d/Q5P9s9s8x1.json"
else:
    period = "Night"
    greeting = "Sweet Dreams! 🌙"
    # Night Gradient (Deep Space Blue)
    bg_gradient = "linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);"
    card_color = "rgba(255, 255, 255, 0.1)"
    text_color = "#e0e0e0"
    lottie_url = "https://lottie.host/a438702b-a010-449e-b7d5-d85202860d5b/b3p2R5s8x1.json"

# --- 4. ADVANCED CSS (The UI Magic) ---
st.markdown(
    f"""
    <style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    /* Global Settings */
    html, body, [class*="css"] {{
        font-family: 'Poppins', sans-serif;
    }}
    
    .stApp {{
        background-image: {bg_gradient};
        background-size: cover;
        background-attachment: fixed;
    }}

    /* Glassmorphism Card Style */
    .glass-card {{
        background: {card_color};
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }}

    /* Text Colors */
    h1, h2, h3, p, label {{
        color: {text_color} !important;
        text-shadow: 0px 2px 4px rgba(0,0,0,0.2);
    }}
    
    /* Stylish Buttons */
    .stButton>button {{
        width: 100%;
        background-color: rgba(255, 255, 255, 0.9);
        color: #333 !important;
        border: none;
        border-radius: 12px;
        padding: 10px 20px;
        font-weight: 600;
        transition: all 0.3s ease;
    }}
    .stButton>button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        background-color: white;
    }}
    
    /* Input Fields styling */
    .stDateInput > div > div > input {{
        background-color: rgba(255,255,255,0.8);
        border-radius: 10px;
        color: black;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- 5. APP LAYOUT WITH GLASS CARDS ---

# Header Section
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.title(f"VibeCal")
st.markdown(f"### {greeting}")
st.write(f"📍 **India Time:** {now.strftime('%I:%M %p')}")
lottie_json = load_lottieurl(lottie_url)
if lottie_json:
    st_lottie(lottie_json, height=180, key="anim")
st.markdown('</div>', unsafe_allow_html=True)

# Celebration Section
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
col_a, col_b = st.columns([3, 1])
with col_a:
    st.markdown("#### 🎉 Special Occasion?")
    st.write("Click if you're celebrating something today!")
with col_b:
    if st.button("Celebrate!"):
        st.balloons()
        st.success("Yay!")
st.markdown('</div>', unsafe_allow_html=True)

# Calendar & AI Section
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown("#### 📅 Your Smart Schedule")
col1, col2 = st.columns(2)

with col1:
    selected_date = st.date_input("Select Date", now)

with col2:
    st.info("💡 **AI Tip:** The stars align for creative work tonight. Write that blog post!")

st.markdown("---")
st.markdown("#### 🤖 AI Social Manager")
st.write("Upcoming: **Client Meeting (Tomorrow)**")

if st.button("Draft WhatsApp Reminder 💬"):
    with st.spinner("AI Agent is thinking..."):
        time.sleep(1)
        st.success("Draft Ready:")
        st.code("Hi! Confirming our meeting for tomorrow at 10 AM. See you there! 🚀", language="text")

st.markdown('</div>', unsafe_allow_html=True)
