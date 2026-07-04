import streamlit as st
from ui.chat_history import show_chat_history
from services.chat_history_service import ChatHistoryService
history = ChatHistoryService()


def show_sidebar(chunks):

    with st.sidebar:

        # ==========================
        # Logo
        # ==========================

        st.markdown("# 🎓 EduBot AI")
        st.caption("Your AI Study Assistant")

        st.divider()

        # ==========================
        # Upload PDFs
        # ==========================

        st.markdown("## 📚 Documents")
        st.caption("Upload one or more educational PDF files")

        uploaded_files = st.file_uploader(
            "Choose PDF(s)",
            type=["pdf"],
            accept_multiple_files=True,
            help="Upload educational PDFs for AI-powered question answering."
        )

        st.divider()
        # ==========================
# Response Language
# ==========================

        st.markdown("## 🌐 Response Language")

        language = st.selectbox(
            "Choose response language",
    [
               "Auto",
               "English",
               "Hindi"
    ],
             key="response_language"
)

        st.divider()

        # ==========================
        # Tips
        # ==========================

        st.markdown("## 💡 Tips")

        st.info(
            """
- 📄 Upload educational PDFs
- 💬 Ask questions
- 📝 Generate summaries
- 🧠 Continue the conversation
"""
        )

        st.divider()

        # ==========================
        # New Chat
        # ==========================

        if st.button(
            "➕ New Chat",
            use_container_width=True
        ):

            # Save current chat before clearing
            if len(st.session_state.get("messages", [])) > 1:

                title = "New Chat"

                for msg in st.session_state.messages:
                    if msg["role"] == "user":
                        title = msg["content"][:40]
                        break

                history.save_chat(
                    title,
                    st.session_state.messages
)

            st.session_state.messages = []
            st.rerun()

        # ==========================
        # Recent Chats
        # ==========================

        if st.session_state.get("chat_sessions"):

            st.divider()

            show_chat_history(
                st.session_state.chat_sessions
            )

        st.divider()

        # ==========================
        # Clear Chat
        # ==========================

        if st.button(
            "🗑 Clear Chat",
            use_container_width=True
        ):
            st.session_state.messages = []
            st.rerun()

        return uploaded_files