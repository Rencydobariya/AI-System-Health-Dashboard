import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import time

from modules.monitor import get_system_data
from modules.risk import calculate_risk, get_suggestion
from modules.ai_chatbot import simple_ai

st.set_page_config(layout="wide")

# Load CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Session
if "chat" not in st.session_state:
    st.session_state.chat = []

# Title
st.markdown("<h1 class='main-title'>🚀 AI System Health Dashboard</h1>", unsafe_allow_html=True)

# Data
data = get_system_data()
risk, trust = calculate_risk(data)
suggestion = get_suggestion(data)

# 🔥 BIG FULL WIDTH PIE CHART
st.markdown("<h2 class='heading'><br>🔥 Live System Usage</h2>", unsafe_allow_html=True)

fig = go.Figure(data=[go.Pie(
    labels=["🧠 CPU", "💾 RAM", "💽 DISK"],
    values=[data["cpu"], data["ram"], data["disk"]],
    hole=0.4,
    textinfo='label+percent',
    textfont_size=22
)])

fig.update_layout(height=600)

st.plotly_chart(fig, use_container_width=True)

# 🔥 BIG VALUES DISPLAY
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"<div class='cpu-box'>🧠 CPU<br><h1>{data['cpu']}%</h1></div>", unsafe_allow_html=True)

with col2:
    st.markdown(f"<div class='ram-box'>💾 RAM<br><h1>{data['ram']}%</h1></div>", unsafe_allow_html=True)

with col3:
    st.markdown(f"<div class='disk-box'>💽 DISK<br><h1>{data['disk']}%</h1></div>", unsafe_allow_html=True)

# 📊 BAR GRAPH (EXTRA VISUAL 🔥)
st.markdown("<h2 class='section-title'><br><br>📊 System Usage Graph</h2>", unsafe_allow_html=True)

bar = px.bar(
    x=["CPU", "RAM", "DISK"],
    y=[data["cpu"], data["ram"], data["disk"]],
    text=[data["cpu"], data["ram"], data["disk"]]
)

bar.update_traces(textposition='outside')

st.plotly_chart(bar, use_container_width=True)

# 🔹 STATUS CARDS
col4, col5, col6 = st.columns(3)

# Risk text
risk_text = "⚠️ HIGH RISK" if risk > 70 else "🚨 RISK"

with col4:
    st.markdown(f"<div class='risk-box'><b>{risk_text}</b><br><h1>{risk}%</h1></div>", unsafe_allow_html=True)

with col5:
    st.markdown(f"<div class='trust-box'>✅ <b>TRUST SCORE<b><br><h1>{trust}%</h1></div>", unsafe_allow_html=True)

with col6:
    st.markdown(f"<div class='suggest-box'>💡 <b>SUGGESTION<b><br><br>{suggestion}<br></div>", unsafe_allow_html=True)

# 🔥 NEW RISK STATUS TEXT (Highlighted)
# 🔥 ANIMATED RISK STATUS TEXT (NO BOX)

if risk < 50:
    risk_status = "🟢 SYSTEM IS SAFE 🚀✨"
    risk_style = "color:#00ff88;"
elif risk < 75:
    risk_status = "🟡 MEDIUM RISK ⚠️ Stay Alert!"
    risk_style = "color:#ffcc00;"
else:
    risk_status = "🔴 HIGH RISK 🚨 TAKE ACTION NOW!"
    risk_style = "color:#ff3333; text-shadow:0 0 20px red;"

st.markdown(f"""
<h1 style="
    margin:50px;       
    text-align:center;
    font-size:45px;
    font-weight:bold;
    {risk_style}
    animation: blink 1s infinite;
">
    ⚡ SYSTEM STATUS: {risk_status}
</h1>
""", unsafe_allow_html=True)

# 🔻 CHATBOT
st.markdown("---")
st.markdown("<h1 class='chat-title'>🤖 AI Chatbot</h1>", unsafe_allow_html=True)

# Buttons
col7, col8 = st.columns(2)
with col7:
    if st.button("🆕 New Chat"):
        st.session_state.chat = []

with col8:
    if st.button("🗑 Clear Chat"):
        st.session_state.chat = []

# Chat history
for chat in st.session_state.chat:
    st.markdown(f"<div class='user-msg'>👤 {chat['user']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='bot-msg'>🤖 {chat['bot']}</div>", unsafe_allow_html=True)

# Input
user_input = st.text_input("Ask something...", key="chat_unique")

if st.button("Send", key="send_unique"):
    if user_input:
        reply = simple_ai(user_input, data)

        st.session_state.chat.append({
            "user": user_input,
            "bot": reply
        })

        st.rerun()

# Auto refresh
time.sleep(3)
st.rerun()
