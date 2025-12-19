import streamlit as st
import datetime
import pytz
import time

# --- 1. SETUP PAGE CONFIG (Must be first) ---
st.set_page_config(page_title="VibeCal: AI Calendar", page_icon="📅", layout="centered")

# --- 2. TIME & THEME LOGIC ---
# Get current time in India
IST = pytz.timezone('Asia/Kolkata')
now = datetime.datetime.now(IST)
current_hour = now.hour

# Define Themes (Colors & Greetings)
if 5 <= current_hour < 12:
    period = "Morning"
    greeting = "Good Morning! ☀️"
    # Soft Orange to Blue Gradient
    bg_gradient = "linear-gradient(to bottom, #FF512F, #DD2476);"
    animation_url = "https://lottie.host/embed/9355462c-6379-44d8-9477-6287950c0576/8YI5Z5vQ7e.json" # Sun
elif 12 <= current_hour < 17:
    period = "Afternoon"
    greeting = "Good Afternoon! 🌤️"
    # Bright Blue Sky
    bg_gradient = "linear-gradient(to bottom, #2980B9, #6DD5FA, #FFFFFF);"
    animation_url = "https://lottie.host/embed/9355462c-6379-44d8-9477-6287950c0576/8YI5Z5vQ7e.json"
elif 17 <= current_hour < 20:
    period = "Evening"
    greeting = "Good Evening! 🌇"
    # Sunset Purple/Pink
    bg_gradient = "linear-gradient(to bottom, #654ea3, #eaafc8);"
    animation_url = "https://lottie.host/embed/8b3f5b72-2d17-48a6-80f6-02607593c78d/Q5P9s9s8x1.json" # Sunset vibe
else:
    period = "Night"
    greeting = "Good Night, Sleep Well! 🌙"
    # Deep Night Blue
    bg_gradient = "linear-gradient(to bottom, #0f2027, #203a43, #2c5364);"
    animation_url = "https://lottie.host/embed/a438702b-a010-449e-b7d5-d85202860d5b/b3p2R5s8x1.json" # Moon

# --- 3. INJECT CSS (The Visual Layer) ---
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: {bg_gradient};
        background-size: cover;
        transition: background 1s ease;
    }}
    /* Make text readable on dark backgrounds */
    h1, h2, h3, p, div, label {{
        color: white !important;
        text-shadow: 1px 1px 2px black;
    }}
    .stButton>button {{
        background-color: white;
        color: black !important;
        border-radius: 10px;
        font-weight: bold;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- 4. APP LAYOUT ---
st.title(f"📅 VibeCal: {period} Edition")
st.markdown(f"### {greeting}")
st.write(f"**Current Time (India):** {now.strftime('%I:%M %p')}")

# Visual Vibe (Animation)
st.components.v1.iframe(src=animation_url, height=200, scrolling=False)

# --- 5. THE CALENDAR & AGENTS (Productivity Layer) ---
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    selected_date = st.date_input("Select Date", now)

with col2:
    st.info("💡 **AI Insight:** It's a clear night. Perfect time to focus on your blog.")

# --- 6. THE FREELANCE DEMO (Social Agent) ---
st.markdown("### 🤖 Social Manager Agent")
st.write("Upcoming Event: **Client Meeting (Tomorrow 10 AM)**")

if st.button("Draft WhatsApp Reminder"):
    with st.spinner("AI Agent is writing..."):
        time.sleep(1.5) # Fake AI delay for effect
        st.success("Draft Generated!")
        st.code(f"Hi! Just confirming our meeting for tomorrow at 10 AM. Looking forward to it! 🚀", language="text")
        st.write("*Click to copy and send!*")

# --- 7. WEATHER ADVISOR (Simple Logic) ---
st.markdown("### ☔ Reality Advisor")
if period == "Night":
    st.warning("🌙 It's getting late. Reduce screen brightness for better sleep.")
elif period == "Morning":
    st.success("☀️ UV Index is high today. Wear sunscreen if going out!")

