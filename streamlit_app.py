import streamlit as st
import datetime
import pytz
import requests
from streamlit_lottie import st_lottie
import time

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="VibeCal: Ultimate", page_icon="✨", layout="centered")

# --- 2. ASSETS & ANIMATIONS (SAFE MODE) ---
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Helper function to prevent crashing if animation fails
def run_animation(url, key_name, height=150):
    data = load_lottieurl(url)
    if data:
        st_lottie(data, height=height, key=key_name)
    else:
        # Fallback if animation fails
        st.warning("⚠️ Animation loading...")

# --- 3. TIME & THEME LOGIC ---
IST = pytz.timezone('Asia/Kolkata')
now = datetime.datetime.now(IST)
hour = now.hour

# Choose Background & Theme based on Time
if 5 <= hour < 12:
    period = "Morning"
    bg_image = "https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?q=80&w=2070"
    greeting = "Good Morning! ☀️"
    glass_color = "rgba(255, 255, 255, 0.25)" 
    text_shadow = "1px 1px 2px black"
elif 12 <= hour < 17:
    period = "Afternoon"
    bg_image = "https://images.unsplash.com/photo-1596524430615-b46475ddff6e?q=80&w=2070"
    greeting = "Focus Mode On 🚀"
    glass_color = "rgba(255, 255, 255, 0.3)"
    text_shadow = "1px 1px 2px black"
elif 17 <= hour < 20:
    period = "Evening"
    bg_image = "https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?q=80&w=2113"
    greeting = "Good Evening 🌆"
    glass_color = "rgba(0, 0, 0, 0.5)" 
    text_shadow = "0px 0px 5px black"
else:
    period = "Night"
    bg_image = "https://images.unsplash.com/photo-1519681393798-2f13fbe68138?q=80&w=2070"
    greeting = "Magical Night ✨"
    glass_color = "rgba(0, 0, 0, 0.6)" 
    text_shadow = "0px 0px 5px black"

# --- 4. ADVANCED CSS ---
st.markdown(
    f"""
    <style>
    .stApp {{
        background: url("{bg_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    h1, h2, h3, h4, h5, h6, p, div, label, span {{
        color: white !important;
        text-shadow: {text_shadow};
        font-family: 'Helvetica Neue', sans-serif;
    }}
    [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {{
        background-color: {glass_color};
        border-radius: 20px;
        padding: 25px;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }}
    .stButton>button {{
        background-color: white;
        color: black !important;
        border-radius: 25px;
        border: none;
        font-weight: bold;
    }}
    input, textarea {{
        background-color: rgba(255, 255, 255, 0.8) !important;
        color: black !important;
        border-radius: 10px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- 5. APP LAYOUT ---

# Header
with st.container():
    st.title(f"{greeting}")
    st.markdown(f"### 🗓️ {now.strftime('%A, %d %B %Y')}")
    st.caption(f"📍 Location: India (IST) • {period} Edition")

# Vibe Controller
st.write("---")
with st.container():
    st.header("🎭 Select Your Vibe")
    
    vibe_mode = st.radio("Choose Scene:", 
                         ["Standard Mode", "🎉 New Year / Party", "🎂 Birthday", "❄️ Winter Snow"], 
                         horizontal=True)

    col_anim, col_msg = st.columns([1, 2])
    
    with col_anim:
        # 1. STANDARD MODE
        if vibe_mode == "Standard Mode":
            if period == "Night":
                run_animation("https://lottie.host/a438702b-a010-449e-b7d5-d85202860d5b/b3p2R5s8x1.json", "moon")
            else:
                run_animation("https://lottie.host/9355462c-6379-44d8-9477-6287950c0576/8YI5Z5vQ7e.json", "sun")

        # 2. NEW YEAR
        elif vibe_mode == "🎉 New Year / Party":
            run_animation("https://lottie.host/80e7228a-7232-4277-b952-4fd77717462c/8h3v5s9x1.json", "fire")
            st.balloons()
        
        # 3. BIRTHDAY
        elif vibe_mode == "🎂 Birthday":
            run_animation("https://lottie.host/1785237c-3225-41d6-857e-12501004f7c2/lqD0b8X9v2.json", "cake")
            st.balloons()
            
        # 4. WINTER
        elif vibe_mode == "❄️ Winter Snow":
            run_animation("https://lottie.host/5d645100-264e-4f0e-920f-08df6c205730/X7u6f3y7v2.json", "snow")
            st.snow()

    with col_msg:
        if vibe_mode == "Standard Mode":
            st.info(f"Currently in **{period} Mode**. Background updated.")
        elif vibe_mode == "🎂 Birthday":
            st.success("Happy Birthday! 🎂")
        elif vibe_mode == "🎉 New Year / Party":
            st.warning("Let's Party! 🎆")
        elif vibe_mode == "❄️ Winter Snow":
            st.info("It's chilly! ☕")

# Connectivity
st.write("---")
with st.container():
    st.header("📲 Connectivity Hub")
    
    c1, c2 = st.columns(2)
    with c1:
        name = st.text_input("Receiver Name", "Client")
        msg = st.text_area("Message Body", f"Hi {name}, hope you have a great {period}!")
    
    with c2:
        st.write("#### Send via:")
        wa_link = f"https://wa.me/?text={msg}"
        mail_link = f"mailto:?subject=VibeCal%20Greeting&body={msg}"
        st.link_button("🚀 Send via WhatsApp", wa_link)
        st.link_button("📧 Send via Email", mail_link)

# Calendar
st.write("---")
with st.container():
    st.header("📅 Smart Schedule")
    d = st.date_input("Plan for:", now)
    
    if st.button("🔮 Generate AI Plan"):
        with st.spinner("AI is thinking..."):
            time.sleep(1.5)
            st.success("AI Plan Generated!")
            st.write("✅ **10:00 AM:** High Focus Work")
            st.write("✅ **01:00 PM:** Team Lunch")
