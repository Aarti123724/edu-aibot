import streamlit as st
from services.chat_history_service import ChatHistoryService
history = ChatHistoryService()


def show_chat_history(chats):

    st.markdown("### 🕒 Recent Chats")

    if not chats:
        st.caption("No chats yet.")
        return

    # Show latest chat first
    for chat in reversed(chats):

        col1, col2 = st.columns([8, 1])

        # -----------------------
        # Open Chat
        # -----------------------
        with col1:

            if st.button(
                f"💬 {chat['title']}",
                key=f"chat_{chat['id']}",
                use_container_width=True
            ):

                st.session_state.messages = chat["messages"].copy()
                st.rerun()

        # -----------------------
        # Delete Chat
        # -----------------------
        with col2:

            if st.button(
                "🗑",
                key=f"delete_{chat['id']}",
                help="Delete this chat"
            ):

                st.session_state.chat_sessions = [
                    c for c in st.session_state.chat_sessions
                    if c["id"] != chat["id"]
                ]

                st.rerun()