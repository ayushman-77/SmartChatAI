import streamlit as st
from script import *

with open("style.css", "r") as file:
    st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

st.markdown("<div class='title'>SmartChatAI</div>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

for role, text in st.session_state.messages:
    if role == "user":
        st.markdown(f"<div class='user-bubble'>{text}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='assistant-bubble'>{text}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

prompt = st.chat_input("Type your message...")

if prompt:
    st.session_state.messages.append(("user", prompt))
    st.markdown(f"<div class='user-bubble'>{prompt}</div>", unsafe_allow_html=True)

    response = generate_response(prompt)
    st.session_state.messages.append(("assistant", response))
    st.markdown(f"<div class='assistant-bubble'>{response}</div>", unsafe_allow_html=True)