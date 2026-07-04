import streamlit as st


class ChatHistoryService:

    def __init__(self):

        if "chat_sessions" not in st.session_state:
            st.session_state.chat_sessions = []

    # ---------------------------------
    # Save Chat
    # ---------------------------------

    def save_chat(self, title, messages):

        chat = {
            "id": len(st.session_state.chat_sessions),
            "title": title,
            "messages": messages.copy()
        }

        st.session_state.chat_sessions.append(chat)

    # ---------------------------------
    # Get All Chats
    # ---------------------------------

    def get_chats(self):

        return st.session_state.chat_sessions

    # ---------------------------------
    # Load Chat
    # ---------------------------------

    def load_chat(self, chat_id):

        for chat in st.session_state.chat_sessions:

            if chat["id"] == chat_id:

                st.session_state.messages = chat["messages"].copy()
                return

    # ---------------------------------
    # Delete Chat
    # ---------------------------------

    def delete_chat(self, chat_id):

        st.session_state.chat_sessions = [

            chat
            for chat in st.session_state.chat_sessions

            if chat["id"] != chat_id

        ]

    # ---------------------------------
    # Rename Chat
    # ---------------------------------

    def rename_chat(self, chat_id, new_title):

        for chat in st.session_state.chat_sessions:

            if chat["id"] == chat_id:

                chat["title"] = new_title
                break

    # ---------------------------------
    # Clear All Saved Chats
    # ---------------------------------

    def clear_history(self):

        st.session_state.chat_sessions = []