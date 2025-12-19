import streamlit as st
import datetime
import pytz
import requests
from streamlit_lottie import st_lottie
import time

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="VibeCal: Ultimate", page_icon="✨", layout="wide")

# --- 2. ASSETS & ANIMATIONS ---
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# --- 3. TIME & SCENARIO LOGIC ---
IST = pytz.timezone('Asia/Kolkata')
now = datetime.datetime.now(IST)
hour = now.hour

# Dynamic Backgrounds (Real Photos)
if 5 <= hour < 12:
    period = "Morning"
    # Morning Landscape Image
    bg_image = "https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?q=80&w=2070&auto=format&fit=crop"
    greeting = "Good Morning! 🌸"
    theme_color = "rgba(255, 255, 255, 0.7)" # Light Glass
    text_color = "#2c3e50"
elif 12 <= hour < 17:
    period = "Afternoon"
    # Bright Blue Sky/Office Image
    bg_image = "https://images.unsplash.com/photo-1596524430615-b46475ddff6e?q=80&w=2070&auto=format&fit=crop"
    greeting = "Focus Mode On 🚀"
    theme_color = "rgba(255, 255, 255, 0.85)"
    text_color = "#1a1a1a"
elif 17 <= hour < 20:
    period = "Evening"
    # Sunset City Image
    bg_image = "https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?q=80&w=2113&auto=format&fit=crop"
    greeting = "Good Evening 🌆"
    theme_color = "rgba(0, 0, 0, 0.6)" # Dark Glass
    text_color = "#ffffff"
else:
    period = "Night"
    # Starry Night or Night City
    bg_image = "https://images.unsplash.com/photo-1519681393798-2f13fbe68138?q=80&w=2070&auto=format&fit=crop"
    greeting = "Magical Night ✨"
    theme_color = "rgba(10, 10, 30, 0.75)" # Deep Dark Glass
    text_color = "#e0e0e0"

# --- 4. CSS FOR IMMERSIVE LOOK ---
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;500;700&display=swap');
    
    .stApp {{
        background: url("{bg_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    
    /* Glassmorphism Container */
    .glass-container {{
        background: {theme_color};
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 25px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 30px;
        margin: 20px auto;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        color: {text_color};
    }}
    
    h1, h2, h3, p, label, div {{
        font-family: 'Montserrat', sans-serif !important;
        color: {text_color} !important;
    }}
    
    /* Button Styling */
    .stButton>button {{
        border-radius: 50px;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }}
    
    /* Hide Default Elements */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    </style>
    """,
    unsafe_allow_html=True
)

# --- 5. THE MAIN INTERFACE ---
col_main, col_padding = st.columns([1, 0.1])

with col_main:
    # --- HEADER SECTION ---
    st.markdown(f'<div class="glass-container">', unsafe_allow_html=True)
    st.title(f"{greeting}")
    st.markdown(f"### {now.strftime('%A, %d %B %Y')}")
    st.caption(f"📍 Location: India • {period} Edition")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- FIREWORKS & FESTIVALS ---
    st.markdown(f'<div class="glass-container">', unsafe_allow_html=True)
    st.markdown("### 🎭 Vibe Controller")
    
    vibe_mode = st.radio("Select Current Vibe:", 
                         ["Standard Mode", "🎉 New Year / Party", "🎂 Birthday", "❄️ Winter Snow"], 
                         horizontal=True)

    if vibe_mode == "🎉 New Year / Party":
        # Fireworks Animation Lottie
        lottie_fireworks = load_lottieurl("https://lottie.host/80e7228a-7232-4277-b952-4fd77717462c/8h3v5s9x1.json")
        if lottie_fireworks:
            st_lottie(lottie_fireworks, height=200, key="fireworks")
        st.balloons()
    
    elif vibe_mode == "❄️ Winter Snow":
        st.snow()
        st.info("Stay warm! ☕")

    st.markdown('</div>', unsafe_allow_html=True)

    # --- CONNECTIVITY CENTER (WhatsApp/Email) ---
    st.markdown(f'<div class="glass-container">', unsafe_allow_html=True)
    st.markdown("### 📲 Connectivity Hub")
    st.write("Connect with people instantly directly from your calendar.")

    col1, col2 = st.columns(2)
    
    # Message Logic
    with col1:
        contact_name = st.text_input("Name", "Client")
        message_body = st.text_area("Message", f"Hi {contact_name}, wishing you a happy {period}!")
    
    with col2:
        st.write("###### Select Platform to Send:")
        
        # WhatsApp Logic (Deep Link)
        whatsapp_url = f"https://wa.me/?text={message_body.replace(' ', '%20')}"
        st.link_button("🚀 Send via WhatsApp", whatsapp_url)
        
        # Email Logic (Deep Link)
        email_url = f"mailto:?subject=Greeting%20from%20VibeCal&body={message_body.replace(' ', '%20')}"
        st.link_button("📧 Send via Email", email_url)
        
        st.markdown("*Note: This opens your secure app directly.*")
    
    st.markdown('</div>', unsafe_allow_html=True)

    # --- CALENDAR & AI ---
    st.markdown(f'<div class="glass-container">', unsafe_allow_html=True)
    st.markdown("### 📅 Smart Schedule")
    d = st.date_input("Plan for:", now)
    
    if st.button("🔮 Ask AI for Day Plan"):
        with st.spinner("Analyzing weather and schedule..."):
            time.sleep(1.5)
            st.success("Plan Generated!")
            if period == "Morning":
                st.write("✅ **10:00 AM:** Deep Work (Energy High)")
                st.write("✅ **01:00 PM:** Lunch & Walk")
            else:
                st.write("✅ **08:00 PM:** Review Goals")
                st.write("✅ **10:00 PM:** Sleep Mode 😴")
    st.markdown('</div>', unsafe_allow_html=True)

