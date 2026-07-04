import streamlit as st


def user_message(message):
    st.markdown(
        f"""
<div class="user-message">
    <div class="chat-title">👤 You</div>
    <div class="chat-content">{message}</div>
</div>
""",
        unsafe_allow_html=True,
    )


def assistant_message(message):
    st.markdown(
        f"""
<div class="assistant-message">
    <div class="chat-title">🤖 EduBot</div>
    <div class="chat-content">{message}</div>
</div>
""",
        unsafe_allow_html=True,
    )