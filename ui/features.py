import streamlit as st


def show_features():

    st.markdown("## ✨ AI Study Tools")

    col1, col2 = st.columns(2)

    with col1:
        st.button("📝 Summary", use_container_width=True)
        st.button("🧠 Flashcards", use_container_width=True)
        st.button("📖 Notes", use_container_width=True)

    with col2:
        st.button("❓ Quiz", use_container_width=True)
        st.button("🎯 Important Qs", use_container_width=True)
        st.button("🗺 Mind Map", use_container_width=True)