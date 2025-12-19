import streamlit as st
import datetime
import pytz

# --- 1. SETUP ---
st.set_page_config(page_title="VibeCal Part 1", page_icon="🎨", layout="centered")

# --- 2. USER SETTINGS (SIDEBAR) ---
# Here we let the user choose their "Personality"
st.sidebar.header("🎨 Appearance")
theme_style = st.sidebar.radio("Choose App Style:", ["🌸 Aesthetic (Girly)", "💼 Business (Pro)"])

# --- 3. THE LIVE INTELLIGENCE ENGINE 🧠 ---
# Calculating Time, Season, and Light
IST = pytz.timezone('Asia/Kolkata')
now = datetime.datetime.now(IST)
hour = now.hour
month = now.month

# A. Day/Night Rotation (Auto-Detect)
if 6 <= hour < 18:
    time_cycle = "Day"
    lighting = "Light"
else:
    time_cycle = "Night"
    lighting = "Dark"

# B. Season/Revolution (Auto-Detect)
if month in [12, 1, 2]:
    season = "Winter ❄️"
elif month in [3, 4, 5]:
    season = "Spring 🌸"
elif month in [6, 7, 8]:
    season = "Summer ☀️"
else:
    season = "Autumn 🍂"

# C. Occasion Logic (Example: New Year)
is_festival = False
festival_name = ""
if now.day == 1 and now.month == 1:
    is_festival = True
    festival_name = "New Year 🎉"

# --- 4. THEME LOGIC (CSS MAGIC) ---

# Default Variables
bg_url = ""
card_bg = ""
text_color = ""
font = ""

# LOGIC: Combine "User Style" + "Time of Day"

if theme_style == "🌸 Aesthetic (Girly)":
    font = "Pacifico, cursive" # Cute font
    if time_cycle == "Day":
        # Day + Aesthetic = Soft Pink/Peach Clouds
        bg_url = "https://images.unsplash.com/photo-1614850523459-c2f4c699c52e?q=80&w=2070"
        card_bg = "rgba(255, 255, 255, 0.4)" # Milky Glass
        text_color = "#4a4a4a"
    else:
        # Night + Aesthetic = Purple Dreamy Stars
        bg_url = "https://images.unsplash.com/photo-1534293507204-0824e4c29415?q=80&w=2070"
        card_bg = "rgba(40, 0, 60, 0.6)" # Purple Glass
        text_color = "#ffe6f2"

elif theme_style == "💼 Business (Pro)":
    font = "Inter, sans-serif" # Clean font
    if time_cycle == "Day":
        # Day + Business = Clean White/Blue Office
        bg_url = "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=2069"
        card_bg = "rgba(255, 255, 255, 0.85)" # White Clean Box
        text_color = "black"
    else:
        # Night + Business = Dark City Skyline
        bg_url = "https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?q=80&w=2113"
        card_bg = "rgba(0, 0, 0, 0.7)" # Black Glass
        text_color = "white"

# Override for Festival (If it's New Year, make it sparkly!)
if is_festival:
    bg_url = "https://images.unsplash.com/photo-1467810563316-b5476525c0f9?q=80&w=2069"

# --- 5. INJECTING THE CSS ---
st.markdown(f"""
    <style>
    /* Import Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;600&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');

    .stApp {{
        background-image: url("{bg_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    .glass-card {{
        background: {card_bg};
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        border: 1px solid rgba(255,255,255, 0.2);
        box-shadow: 0 4px 30px rgba(0,0,0,0.1);
    }}
    
    h1, h2, h3, p {{
        color: {text_color} !important;
        font-family: {font};
    }}
    </style>
""", unsafe_allow_html=True)

# --- 6. DISPLAYING THE UI ---

# Center Layout
c1, c2, c3 = st.columns([1, 6, 1])

with c2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    # 1. Clock Display
    st.title(now.strftime('%I:%M %p'))
    
    # 2. Date Display
    st.markdown(f"### {now.strftime('%A, %d %B')}")
    st.caption(f"📍 India | {time_cycle}")
    
    st.markdown("---")
    
    # 3. Live Environment Status
    if is_festival:
        st.header(f"🎉 {festival_name}")
        st.write("Special festive theme applied!")
    else:
        st.write(f"Current Season: **{season}**")
        if theme_style == "🌸 Aesthetic (Girly)":
            st.write("✨ Feeling cute & productive!")
        else:
            st.write("🚀 Ready for business.")

    st.markdown('</div>', unsafe_allow_html=True)

