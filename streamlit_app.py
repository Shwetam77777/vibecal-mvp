import streamlit as st
import datetime
import pytz
import calendar
import urllib.parse # For formatting WhatsApp messages

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="VibeCal OS", page_icon="✨", layout="centered")

# --- 2. SIDEBAR NAVIGATION & THEME ---
st.sidebar.title("💎 VibeCal OS")
st.sidebar.header("🧭 Navigation")
page = st.sidebar.radio("Go to:", ["🏠 Home (Calendar)", "🤖 Work Zone", "📲 Social Connect"])

st.sidebar.markdown("---")
st.sidebar.header("🎨 Appearance")
theme_style = st.sidebar.selectbox(
    "Select Theme:",
    ["🌸 Aesthetic (Girly)", "💼 Business (Pro)", "🖤 Dark Mode (Cyber)"]
)

# --- 3. INTELLIGENCE ENGINE 🧠 ---
IST = pytz.timezone('Asia/Kolkata')
now = datetime.datetime.now(IST)
current_year = now.year
current_month = now.month
today_date = now.day
hour = now.hour

# Memory for Tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Day/Night Check
time_cycle = "Day" if 6 <= hour < 18 else "Night"

# --- 4. VISUAL ENGINE (CSS STYLES) ---
# Default Variables
bg_url = ""
glass_color = ""
text_color = ""
highlight_color = ""
font = "sans-serif"
btn_color = ""

# THEME LOGIC
if theme_style == "🌸 Aesthetic (Girly)":
    font = "Pacifico, cursive"
    highlight_color = "#ff69b4" # Hot Pink
    btn_color = "linear-gradient(45deg, #ff9a9e 0%, #fad0c4 99%, #fad0c4 100%)"
    if time_cycle == "Day":
        bg_url = "https://images.unsplash.com/photo-1614850523459-c2f4c699c52e?q=80&w=2070"
        glass_color = "rgba(255, 255, 255, 0.4)"
        text_color = "#4a4a4a"
    else:
        bg_url = "https://images.unsplash.com/photo-1534293507204-0824e4c29415?q=80&w=2070"
        glass_color = "rgba(60, 20, 80, 0.6)"
        text_color = "#ffe6f2"

elif theme_style == "💼 Business (Pro)":
    font = "Inter, sans-serif"
    highlight_color = "#007bff" # Blue
    btn_color = "linear-gradient(120deg, #89f7fe 0%, #66a6ff 100%)"
    if time_cycle == "Day":
        bg_url = "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=2069"
        glass_color = "rgba(255, 255, 255, 0.9)"
        text_color = "#000000"
    else:
        bg_url = "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=2070"
        glass_color = "rgba(0, 0, 0, 0.8)"
        text_color = "#ffffff"

elif theme_style == "🖤 Dark Mode (Cyber)":
    font = "Courier New, monospace"
    highlight_color = "#00ff41" # Neon Green
    btn_color = "linear-gradient(to right, #0f2027, #203a43, #2c5364)"
    bg_url = "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=2070"
    glass_color = "rgba(0, 0, 0, 0.9)"
    text_color = "#00ff41"

# INJECT CSS
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;600&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');

    .stApp {{
        background-image: url("{bg_url}");
        background-size: cover;
        background-attachment: fixed;
    }}
    .glass-card {{
        background: {glass_color};
        backdrop-filter: blur(12px);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        border: 1px solid rgba(255,255,255,0.2);
        color: {text_color};
    }}
    h1, h2, h3, p, div, span, label {{
        font-family: {font};
        color: {text_color} !important;
    }}
    
    /* Calendar Styling */
    .cal-container {{ display: grid; grid-template-columns: repeat(7, 1fr); gap: 5px; margin-top: 10px; }}
    .cal-header {{ font-weight: bold; font-size: 0.8rem; text-align: center; }}
    .cal-day {{ padding: 10px; border-radius: 8px; text-align: center; font-size: 0.9rem; }}
    .today-highlight {{ background-color: {highlight_color}; color: white !important; font-weight: bold; box-shadow: 0 0 10px {highlight_color}; }}
    
    /* Button Styling */
    .stButton>button {{
        background-image: {btn_color};
        color: white;
        border: none;
        border-radius: 10px;
        width: 100%;
    }}
    </style>
""", unsafe_allow_html=True)

# --- 5. MAIN PAGE LAYOUT ---

c1, c2, c3 = st.columns([1, 6, 1])

with c2:
    
    # === PAGE 1: HOME ===
    if page == "🏠 Home (Calendar)":
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.title(now.strftime('%I:%M %p'))
        st.markdown(f"### {now.strftime('%A, %d %B')}")
        st.caption("Daily Overview")
        st.markdown("---")
        
        st.write("#### 🗓️ This Month")
        cal = calendar.monthcalendar(current_year, current_month)
        days = ['M', 'T', 'W', 'T', 'F', 'S', 'S']
        
        html = '<div class="cal-container">'
        for d in days:
            html += f'<div class="cal-header">{d}</div>'
        for week in cal:
            for day in week:
                if day == 0:
                    html += '<div></div>'
                elif day == today_date:
                    html += f'<div class="cal-day today-highlight">{day}</div>'
                else:
                    html += f'<div class="cal-day">{day}</div>'
        html += '</div>'
        st.markdown(html, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # === PAGE 2: WORK ZONE ===
    elif page == "🤖 Work Zone":
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.title("🤖 Task Manager")
        st.write("Stay productive.")
        st.markdown("---")
        
        with st.form("task_form", clear_on_submit=True):
            new_task = st.text_input("📝 Add Task:", placeholder="Type here...")
            if st.form_submit_button("Add Goal"):
                if new_task:
                    st.session_state.tasks.append({"title": new_task, "done": False})
                    st.rerun()
        
        if st.session_state.tasks:
            st.write("### 📋 To-Do List")
            for i, task in enumerate(st.session_state.tasks):
                st.checkbox(task["title"], key=f"task_{i}")
            
            if st.button("🗑️ Clear All"):
                st.session_state.tasks = []
                st.rerun()
        else:
            st.info("No tasks pending!")
        st.markdown('</div>', unsafe_allow_html=True)

    # === PAGE 3: SOCIAL CONNECT (NEW!) ===
    elif page == "📲 Social Connect":
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.title("📲 Connect Hub")
        st.write("Send quick updates to clients/family.")
        st.markdown("---")
        
        # 1. Message Composer
        contact_num = st.text_input("📞 Phone Number (Optional)", placeholder="e.g. 919876543210")
        message = st.text_area("✍️ Type Message", f"Hi! Just checking in. Today is {now.strftime('%A')}.")
        
        # 2. Encode Message for URL
        encoded_msg = urllib.parse.quote(message)
        
        # 3. Dynamic Links
        col_wa, col_mail = st.columns(2)
        
        with col_wa:
            if contact_num:
                wa_link = f"https://wa.me/{contact_num}?text={encoded_msg}"
            else:
                wa_link = f"https://wa.me/?text={encoded_msg}" # Lets user pick contact
            
            st.link_button("🚀 WhatsApp", wa_link, use_container_width=True)
            
        with col_mail:
            mail_link = f"mailto:?body={encoded_msg}&subject=Update from VibeCal"
            st.link_button("📧 Email", mail_link, use_container_width=True)
            
        st.caption("Note: Clicking WhatsApp will open the app/web directly.")
        st.markdown('</div>', unsafe_allow_html=True)

