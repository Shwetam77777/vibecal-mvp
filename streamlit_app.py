import streamlit as st
import datetime
import pytz
import requests
from streamlit_lottie import st_lottie

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="VibeCal OS", page_icon="🌍", layout="centered")

# --- 2. ASSETS & ANIMATION LOADER ---
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

def run_animation(url, height=150, key="anim"):
    data = load_lottieurl(url)
    if data:
        st_lottie(data, height=height, key=key)

# --- 3. THE LIVE INTELLIGENCE ENGINE 🧠 ---

IST = pytz.timezone('Asia/Kolkata')
now = datetime.datetime.now(IST)
current_month = now.month
current_hour = now.hour

# A. Season Logic (Dec = Winter)
if current_month in [12, 1, 2]:
    season = "Winter"
    season_emoji = "❄️"
    # Pretty Snow Animation
    season_anim = "https://lottie.host/5d645100-264e-4f0e-920f-08df6c205730/X7u6f3y7v2.json"
elif current_month in [3, 4, 5]:
    season = "Spring"
    season_emoji = "🌸"
    season_anim = "https://lottie.host/4933a925-5e6e-41df-a524-7eb32662058e/s6y3w8Yj9w.json"
elif current_month in [6, 7, 8]:
    season = "Summer"
    season_emoji = "☀️"
    season_anim = "https://lottie.host/9355462c-6379-44d8-9477-6287950c0576/8YI5Z5vQ7e.json"
else:
    season = "Autumn"
    season_emoji = "🍂"
    season_anim = "https://lottie.host/6e4092d6-1135-420a-b223-9565507c5a03/p1v7S9x3k2.json"

# B. Time Logic (Backgrounds)
if 5 <= current_hour < 12:
    period = "Morning"
    bg_image = "https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?q=80&w=2070"
elif 12 <= current_hour < 17:
    period = "Afternoon"
    bg_image = "https://images.unsplash.com/photo-1596524430615-b46475ddff6e?q=80&w=2070"
elif 17 <= current_hour < 20:
    period = "Evening"
    bg_image = "https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?q=80&w=2113"
else:
    period = "Night"
    bg_image = "https://images.unsplash.com/photo-1519681393798-2f13fbe68138?q=80&w=2070"

# --- 4. PREMIUM CSS (DARK GLASS THEME) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;600&display=swap');
    
    /* Background Image */
    .stApp {{
        background-image: url("{bg_image}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* Global Font */
    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
    }}

    /* DARK GLASS CARD (The Fix) */
    .premium-card {{
        background: rgba(0, 0, 0, 0.6); /* Darker background for contrast */
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 40px;
        text-align: center;
        box-shadow: 0 10px 40px rgba(0,0,0,0.5);
        color: white;
        max-width: 500px;
        margin: auto;
    }}

    /* Typography */
    h1 {{
        color: white !important;
        font-weight: 600;
        letter-spacing: -1px;
        margin-bottom: 0px;
    }}
    p {{
        color: #e0e0e0 !important;
        font-size: 1.1rem;
    }}
    hr {{
        border-color: rgba(255,255,255,0.2);
    }}
    
    /* Hide Streamlit Elements */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    </style>
""", unsafe_allow_html=True)

# --- 5. VISUAL LAYOUT ---

# Using columns to center the card perfectly
c1, c2, c3 = st.columns([1, 6, 1])

with c2:
    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    
    # Time Display
    st.title(now.strftime('%I:%M %p'))
    st.caption(f"{now.strftime('%A, %d %B')} | 📍 India")
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Live Environment Status
    st.markdown(f"### {season} Season {season_emoji}")
    st.write(f"The vibe is currently **{period}**.")
    
    # Animation (Centered)
    run_animation(season_anim, height=180)
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- 6. TEST TOOLS (Sidebar) ---
with st.sidebar:
    st.header("🛠️ Developer Tools")
    if st.button("Test Winter ❄️"):
        st.snow()
    if st.button("Test Celebration 🎉"):
        st.balloons()
