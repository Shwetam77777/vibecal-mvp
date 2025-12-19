import streamlit as st
import datetime
import pytz
import requests
from streamlit_lottie import st_lottie
import time

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="VibeCal: Ultimate", page_icon="✨", layout="centered")

# --- 2. ASSETS & ANIMATIONS ---
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
hour = now.hour

# Choose Background & Theme based on Time
if 5 <= hour < 12:
    period = "Morning"
    # Morning Mountain View
    bg_image = "https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?q=80&w=2070"
    greeting = "Good Morning! ☀️"
    glass_color = "rgba(255, 255, 255, 0.25)" # Light Glass
    text_shadow = "1px 1px 2px black"
elif 12 <= hour < 17:
    period = "Afternoon"
    # Bright Sky View
    bg_image = "https://images.unsplash.com/photo-1596524430615-b46475ddff6e?q=80&w=2070"
    greeting = "Focus Mode On 🚀"
    glass_color = "rgba(255, 255, 255, 0.3)"
    text_shadow = "1px 1px 2px black"
elif 17 <= hour < 20:
    period = "Evening"
    # Sunset View
    bg_image = "https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?q=80&w=2113"
    greeting = "Good Evening 🌆"
    glass_color = "rgba(0, 0, 0, 0.5)" # Dark Glass
    text_shadow = "0px 0px 5px black"
else:
    period = "Night"
    # Night Sky View
    bg_image = "https://images.unsplash.com/photo-1519681393798-2f13fbe68138?q=80&w=2070"
    greeting = "Magical Night ✨"
    glass_color = "rgba(0, 0, 0, 0.6)" # Darker Glass
    text_shadow = "0px 0px 5px black"

# --- 4. ADVANCED CSS (Visual Styling) ---
st.markdown(
    f"""
    <style>
    /* 1. Background Image */
    .stApp {{
        background: url("{bg_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    
    /* 2. Text Styling (White & readable) */
    h1, h2, h3, h4, h5, h6, p, div, label, span {{
        color: white !important;
        text-shadow: {text_shadow};
        font-family: 'Helvetica Neue', sans-serif;
    }}
    
    /* 3. Glass Containers (The Blocks) */
    [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {{
        background-color: {glass_color};
        border-radius: 20px;
        padding: 25px;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }}

    /* 4. Button Styling */
    .stButton>button {{
        background-color: white;
        color: black !important;
        border-radius: 25px;
        border: none;
        font-weight: bold;
        text-shadow: none;
        transition: transform 0.2s;
    }}
    .stButton>button:hover {{
        transform: scale(1.05);
    }}
    
    /* 5. Input Fields */
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

# --- HEADER SECTION ---
with st.container():
    st.title(f"{greeting}")
    st.markdown(f"### 🗓️ {now.strftime('%A, %d %B %Y')}")
    st.caption(f"📍 Location: India (IST) • {period} Edition")

# --- VIBE CONTROLLER (Fireworks & Birthday Logic) ---
st.write("---")
with st.container():
    st.header("🎭 Select Your Vibe")
    
    # The Radio Button
    vibe_mode = st.radio("Choose Scene:", 
                         ["Standard Mode", "🎉 New Year / Party", "🎂 Birthday", "❄️ Winter Snow"], 
                         horizontal=True)

    col_anim, col_msg = st.columns([1, 2])
    
    with col_anim:
        # 1. STANDARD MODE (Sun/Moon)
        if vibe_mode == "Standard Mode":
            if period == "Night":
                # Moon Animation
                st_lottie(load_lottieurl("https://lottie.host/a438702b-a010-449e-b7d5-d85202860d5b/b3p2R5s8x1.json"), height=150, key="moon")
            else:
                # Sun Animation
                st_lottie(load_lottieurl("https://lottie.host/9355462c-6379-44d8-9477-6287950c0576/8YI5Z5vQ7e.json"), height=150, key="sun")

        # 2. NEW YEAR (Fireworks!)
        elif vibe_mode == "🎉 New Year / Party":
            # Fireworks Animation
            st_lottie(load_lottieurl("https://lottie.host/80e7228a-7232-4277-b952-4fd77717462c/8h3v5s9x1.json"), height=150, key="fire")
            st.balloons()
        
        # 3. BIRTHDAY (Cake!)
        elif vibe_mode == "🎂 Birthday":
            # Cake Animation
            st_lottie(load_lottieurl("https://lottie.host/1785237c-3225-41d6-857e-12501004f7c2/lqD0b8X9v2.json"), height=150, key="cake")
            st.balloons()
            
        # 4. WINTER (Snow!)
        elif vibe_mode == "❄️ Winter Snow":
            # Snowman Animation
            st_lottie(load_lottieurl("https://lottie.host/5d645100-264e-4f0e-920f-08df6c205730/X7u6f3y7v2.json"), height=150, key="snow")
            st.snow()

    with col_msg:
        if vibe_mode == "Standard Mode":
            st.info(f"Currently in **{period} Mode**. Background updated automatically.")
        elif vibe_mode == "🎂 Birthday":
            st.success("Happy Birthday! 🎂 Sending you best wishes!")
        elif vibe_mode == "🎉 New Year / Party":
            st.warning("Let's Party! 🎆 Fireworks deployed.")
        elif vibe_mode == "❄️ Winter Snow":
            st.info("It's chilly! ☕ Enjoy the snowfall.")

# --- CONNECTIVITY HUB ---
st.write("---")
with st.container():
    st.header("📲 Connectivity Hub")
    st.write("Draft and send messages instantly.")
    
    c1, c2 = st.columns(2)
    with c1:
        name = st.text_input("Receiver Name", "Client")
        msg = st.text_area("Message Body", f"Hi {name}, hope you have a great {period}!")
    
    with c2:
        st.write("#### Send via:")
        # Deep Links (No API Key needed)
        wa_link = f"https://wa.me/?text={msg}"
        mail_link = f"mailto:?subject=VibeCal%20Greeting&body={msg}"
        
        st.link_button("🚀 Send via WhatsApp", wa_link)
        st.link_button("📧 Send via Email", mail_link)

# --- CALENDAR SECTION ---
st.write("---")
with st.container():
    st.header("📅 Smart Schedule")
    d = st.date_input("Plan for:", now)
    
    if st.button("🔮 Generate AI Plan"):
        with st.spinner("AI is thinking..."):
            time.sleep(1.5)
            st.success("AI Plan Generated!")
            if period == "Morning":
                st.write("✅ **10:00 AM:** High Focus Work")
                st.write("✅ **01:00 PM:** Team Lunch")
            else:
                st.write("✅ **08:00 PM:** Review Goals")
                st.write("✅ **10:30 PM:** Wind Down & Read")

