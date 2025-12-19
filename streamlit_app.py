import streamlit as st
import datetime
import pytz
import requests
from streamlit_lottie import st_lottie

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="VibeCal: Live Universe", page_icon="🌍", layout="wide")

# --- 2. ASSETS & ANIMATION LOADER ---
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

def run_animation(url, height=200, key="anim"):
    data = load_lottieurl(url)
    if data:
        st_lottie(data, height=height, key=key)

# --- 3. THE INTELLIGENCE ENGINE (Time + Season + Festival) 🧠 ---

IST = pytz.timezone('Asia/Kolkata')
now = datetime.datetime.now(IST)
today = now.date()
current_hour = now.hour
current_month = now.month

# A. Determine Season (Revolution)
if current_month in [12, 1, 2]:
    season = "Winter"
    season_icon = "❄️"
    season_anim = "https://lottie.host/5d645100-264e-4f0e-920f-08df6c205730/X7u6f3y7v2.json" # Snow
elif current_month in [3, 4, 5]:
    season = "Spring"
    season_icon = "🌸"
    season_anim = "https://lottie.host/4933a925-5e6e-41df-a524-7eb32662058e/s6y3w8Yj9w.json" # Flowers
elif current_month in [6, 7, 8]:
    season = "Summer"
    season_icon = "☀️"
    season_anim = "https://lottie.host/9355462c-6379-44d8-9477-6287950c0576/8YI5Z5vQ7e.json" # Sun
else:
    season = "Autumn"
    season_icon = "🍂"
    season_anim = "https://lottie.host/6e4092d6-1135-420a-b223-9565507c5a03/p1v7S9x3k2.json" # Leaves

# B. Determine Time of Day (Rotation)
if 5 <= current_hour < 12:
    period = "Morning"
    greeting = "Rise & Shine"
    bg_image = "https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?q=80&w=2070" # Sunrise
elif 12 <= current_hour < 17:
    period = "Afternoon"
    greeting = "Focus Mode"
    bg_image = "https://images.unsplash.com/photo-1604079628040-94301bb21b91?q=80&w=2070" # Bright Sky
elif 17 <= current_hour < 20:
    period = "Evening"
    greeting = "Good Evening"
    bg_image = "https://images.unsplash.com/photo-1505322022379-7c3353ee6291?q=80&w=2000" # Sunset
else:
    period = "Night"
    greeting = "Sweet Dreams"
    bg_image = "https://images.unsplash.com/photo-1506318137071-a8bcbf6755dd?q=80&w=2070" # Stars

# C. Festival Override (The Special Logic)
festival_mode = False
festival_name = ""

if today.month == 1 and today.day == 1:
    festival_mode = True
    festival_name = "New Year"
    bg_image = "https://images.unsplash.com/photo-1467810563316-b5476525c0f9?q=80&w=2069" # Fireworks Sky
    season_anim = "https://lottie.host/80e7228a-7232-4277-b952-4fd77717462c/8h3v5s9x1.json" # Fireworks Lottie

elif today.month == 12 and today.day == 25:
    festival_mode = True
    festival_name = "Christmas"
    # Christmas Background

# --- 4. CSS STYLING (Glassmorphism) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap');
    
    .stApp {{
        background-image: url("{bg_image}");
        background-size: cover;
        background-attachment: fixed;
        font-family: 'Poppins', sans-serif;
    }}
    
    /* Glass Card */
    .glass {{
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 30px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    }}
    
    h1 {{ text-shadow: 0 2px 4px rgba(0,0,0,0.5); font-weight: 600; }}
    p {{ text-shadow: 0 1px 2px rgba(0,0,0,0.5); }}
    </style>
""", unsafe_allow_html=True)

# --- 5. VISUAL LAYOUT (Testing Part 1) ---

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Main Glass Card
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    
    # 1. Display Greeting & Time
    st.title(f"{greeting}!")
    st.markdown(f"### {now.strftime('%I:%M %p')}")
    st.caption(f"📍 India • {period}")
    
    st.markdown("---")
    
    # 2. Display The Live Environment (Season/Festival)
    if festival_mode:
        st.markdown(f"## 🎉 It's {festival_name}!")
        run_animation(season_anim, height=200)
        st.balloons()
    else:
        st.markdown(f"### Season: {season} {season_icon}")
        st.write(f"The environment is set to **{season}** based on real data.")
        # Play the Season Animation (Snow/Sun/Flowers)
        run_animation(season_anim, height=180)

    st.markdown('</div>', unsafe_allow_html=True)

# --- 6. DEVELOPER TOOLS (Test The Seasons) ---
with st.sidebar:
    st.header("🛠️ God Mode (Test)")
    st.write("Override the real sensors to test visuals:")
    
    if st.button("❄️ Test Winter"):
        st.snow()
    if st.button("🎆 Test New Year"):
        st.balloons()

