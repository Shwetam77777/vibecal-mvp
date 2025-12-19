import streamlit as st
import datetime
import pytz
import requests
from streamlit_lottie import st_lottie
import time

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="VibeCal: Real Auto", page_icon="📅", layout="centered")

# --- 2. SAFETY ANIMATION LOADER ---
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

def run_animation(url, height=150):
    data = load_lottieurl(url)
    if data:
        st_lottie(data, height=height)
    else:
        st.warning("⚠️ Loading visual...")

# --- 3. REAL TIME & DATE INTELLIGENCE ---
IST = pytz.timezone('Asia/Kolkata')
now = datetime.datetime.now(IST)
today_date = now.date()
current_hour = now.hour

# --- 4. AUTO-DETECT EVENT LOGIC (The Brain) 🧠 ---
# Default Vibe
vibe = "Standard"
event_msg = f"Today is {now.strftime('%A, %d %B')}."

# Check for Special Dates (Automatic)
if today_date.month == 1 and today_date.day == 1:
    vibe = "New Year"
    event_msg = "🎉 Happy New Year! Welcome to 2026!"
elif today_date.month == 12 and today_date.day == 25:
    vibe = "Christmas"
    event_msg = "🎄 Merry Christmas!"
elif today_date.month == 10 and today_date.day == 20: # Example Diwali Date
    vibe = "Diwali"
    event_msg = "🪔 Happy Diwali!"
# Add your birthday here (Example: Dec 25)
elif today_date.month == 12 and today_date.day == 20: 
    vibe = "Birthday"
    event_msg = "🎂 Happy Birthday Shweta!"

# --- 5. TEST MODE (To show clients fireworks anytime) ---
with st.sidebar:
    st.header("🛠️ Developer Tools")
    test_mode = st.checkbox("Force Test Event")
    if test_mode:
        vibe = st.selectbox("Simulate Event:", ["New Year", "Birthday", "Christmas", "Standard"])
        event_msg = f"Simulating: {vibe}"

# --- 6. BACKGROUND LOGIC ---
if 5 <= current_hour < 12:
    period = "Morning"
    bg_image = "https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?q=80&w=2070"
    greeting = "Good Morning!"
elif 12 <= current_hour < 17:
    period = "Afternoon"
    bg_image = "https://images.unsplash.com/photo-1596524430615-b46475ddff6e?q=80&w=2070"
    greeting = "Focus Mode On"
elif 17 <= current_hour < 20:
    period = "Evening"
    bg_image = "https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?q=80&w=2113"
    greeting = "Good Evening"
else:
    period = "Night"
    bg_image = "https://images.unsplash.com/photo-1519681393798-2f13fbe68138?q=80&w=2070"
    greeting = "Good Night"

# --- 7. CSS STYLING ---
st.markdown(
    f"""
    <style>
    .stApp {{
        background: url("{bg_image}");
        background-size: cover;
        background-attachment: fixed;
    }}
    h1, h2, h3, p, div, span, label {{
        color: white !important;
        text-shadow: 0px 1px 3px rgba(0,0,0,0.8);
    }}
    /* Glass Container */
    [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {{
        background-color: rgba(255, 255, 255, 0.15);
        border-radius: 15px;
        padding: 20px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- 8. MAIN DISPLAY ---

with st.container():
    st.title(f"{greeting}")
    st.markdown(f"### 🗓️ {now.strftime('%A, %d %B %Y')}")
    st.write(f"**Status:** {event_msg}")

    # AUTO-PLAY ANIMATIONS (No Buttons Needed)
    if vibe == "New Year":
        run_animation("https://lottie.host/80e7228a-7232-4277-b952-4fd77717462c/8h3v5s9x1.json") # Fireworks
        st.balloons() # Real Balloons
    elif vibe == "Birthday":
        run_animation("https://lottie.host/1785237c-3225-41d6-857e-12501004f7c2/lqD0b8X9v2.json") # Cake
        st.balloons()
    elif vibe == "Christmas":
        run_animation("https://lottie.host/5d645100-264e-4f0e-920f-08df6c205730/X7u6f3y7v2.json") # Snow
        st.snow()
    else:
        # Standard Sun/Moon
        if period == "Night":
            run_animation("https://lottie.host/a438702b-a010-449e-b7d5-d85202860d5b/b3p2R5s8x1.json")
        else:
            run_animation("https://lottie.host/9355462c-6379-44d8-9477-6287950c0576/8YI5Z5vQ7e.json")

# --- 9. REAL CALENDAR DISPLAY ---
st.write("---")
with st.container():
    st.header("📅 Your Schedule")
    
    # Simple Calendar Grid Layout
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # User picks a date to view
        d = st.date_input("Go to Date:", today_date)
    
    with col2:
        # Dynamic Schedule Display
        st.write(f"**Events for {d.strftime('%d %B')}:**")
        
        if d.month == 1 and d.day == 1:
            st.success("🎉 12:00 AM - New Year Celebration")
            st.info("🗓️ 11:00 AM - Family Lunch")
        elif d == today_date:
            st.info("🕒 09:00 AM - Working on TechNova Blog")
            st.info("🕒 02:00 PM - VibeCal Testing")
            st.warning("🕒 06:00 PM - Freelance Client Search")
        else:
            st.write("No events scheduled yet.")
            if st.button("➕ Add Event"):
                st.toast("Event Saved!")

# --- 10. CONNECTIVITY ---
st.write("---")
with st.container():
    st.header("📲 Quick Connect")
    c1, c2 = st.columns(2)
    with c1:
        msg = st.text_input("Quick Message:", "Hi! Happy New Year!")
    with c2:
        st.write("") # Spacer
        st.link_button("🚀 Send via WhatsApp", f"https://wa.me/?text={msg}")

