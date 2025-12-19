import streamlit as st
import datetime
import pytz

# --- 1. SETUP ---
st.set_page_config(page_title="VibeCal OS", page_icon="🎨", layout="centered")

# --- 2. THEME SELECTOR ---
st.sidebar.header("🎨 Design Studio")
theme_style = st.sidebar.selectbox(
    "Select Your Vibe:",
    ["🌸 Aesthetic (Girly)", "💼 Business (Pro)", "🌿 Nature (Live Season)", "🖤 Dark Mode (Cyber)"]
)

# --- 3. INTELLIGENCE ENGINE (Time & Season) 🧠 ---
IST = pytz.timezone('Asia/Kolkata')
now = datetime.datetime.now(IST)
hour = now.hour
month = now.month

# A. Day/Night Check
if 6 <= hour < 18:
    time_cycle = "Day"
else:
    time_cycle = "Night"

# B. Season Check
if month in [12, 1, 2]:
    season_name = "Winter"
    season_emoji = "❄️"
elif month in [3, 4, 5]:
    season_name = "Spring"
    season_emoji = "🌸"
elif month in [6, 7, 8]:
    season_name = "Summer"
    season_emoji = "☀️"
else:
    season_name = "Autumn"
    season_emoji = "🍂"

# --- 4. VISUAL ENGINE (The Look) ---

# Default Variables
bg_url = ""
glass_color = ""
text_color = ""
font = "sans-serif"
border_color = "rgba(255,255,255,0.2)"

# --- THEME 1: AESTHETIC (Girly/Soft) ---
if theme_style == "🌸 Aesthetic (Girly)":
    font = "Pacifico, cursive"
    if time_cycle == "Day":
        bg_url = "https://images.unsplash.com/photo-1614850523459-c2f4c699c52e?q=80&w=2070" # Soft Pink Clouds
        glass_color = "rgba(255, 255, 255, 0.4)"
        text_color = "#4a4a4a"
    else:
        bg_url = "https://images.unsplash.com/photo-1534293507204-0824e4c29415?q=80&w=2070" # Purple Stars
        glass_color = "rgba(60, 20, 80, 0.6)"
        text_color = "#ffe6f2"

# --- THEME 2: BUSINESS (Professional) ---
elif theme_style == "💼 Business (Pro)":
    font = "Inter, sans-serif"
    if time_cycle == "Day":
        bg_url = "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=2069" # White Office
        glass_color = "rgba(255, 255, 255, 0.9)"
        text_color = "#000000"
    else:
        bg_url = "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=2070" # City Skyscrapers
        glass_color = "rgba(0, 0, 0, 0.8)"
        text_color = "#ffffff"

# --- THEME 3: NATURE (Focus on Seasons) ---
elif theme_style == "🌿 Nature (Live Season)":
    font = "Georgia, serif"
    # Background changes based on SEASON, not just time
    if season_name == "Winter":
        bg_url = "https://images.unsplash.com/photo-1483921020237-60f29bf9f430?q=80&w=2000" # Snow
    elif season_name == "Summer":
        bg_url = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=2000" # Beach
    elif season_name == "Spring":
        bg_url = "https://images.unsplash.com/photo-1490750967868-58cb75069ed6?q=80&w=2000" # Flowers
    else:
        bg_url = "https://images.unsplash.com/photo-1506744038136-46273834b3fb?q=80&w=2000" # Autumn
        
    glass_color = "rgba(0, 0, 0, 0.5)" # Darker glass to see nature
    text_color = "#ffffff"

# --- THEME 4: DARK MODE (Cyber/Hacker) ---
elif theme_style == "🖤 Dark Mode (Cyber)":
    font = "Courier New, monospace"
    bg_url = "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=2070" # Matrix/Cyber code
    glass_color = "rgba(0, 0, 0, 0.9)"
    text_color = "#00ff41" # Matrix Green
    border_color = "#00ff41" # Neon Border

# --- 5. INJECT CSS ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;600&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');

    .stApp {{
        background-image: url("{bg_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    .glass-card {{
        background: {glass_color};
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 20px;
        border: 1px solid {border_color};
        padding: 40px;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }}
    
    h1, h2, h3, p, span {{
        color: {text_color} !important;
        font-family: {font};
    }}
    </style>
""", unsafe_allow_html=True)

# --- 6. DISPLAY UI ---
# Centered Layout
c1, c2, c3 = st.columns([1, 6, 1])

with c2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    # Time & Date
    st.title(now.strftime('%I:%M %p'))
    st.markdown(f"### {now.strftime('%A, %d %B')}")
    st.caption(f"📍 India | {time_cycle} | {season_name}")
    
    st.markdown("---")
    
    # Theme Specific Message
    if theme_style == "🌸 Aesthetic (Girly)":
        st.write("✨ Create your own magic today.")
    elif theme_style == "💼 Business (Pro)":
        st.write("📈 Productivity levels optimal.")
    elif theme_style == "🌿 Nature (Live Season)":
        st.write(f"Enjoy the {season_name} vibes {season_emoji}")
    elif theme_style == "🖤 Dark Mode (Cyber)":
        st.write("> SYSTEM.READY_TO_CODE_")

    st.markdown('</div>', unsafe_allow_html=True)

# --- 7. DEVELOPER NOTE ---
with st.sidebar:
    st.info(f"Current Season Detected: **{season_name}**")
