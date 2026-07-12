import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from services.rag_service import RAGService
from classifier import is_education_question
from pdf_utils import extract_pdf_text
from rag_utils import split_documents
# from gemini_ocr import extract_text_with_gemini
from services.summary_service import generate_summary
from services.chat_service import generate_answer
from services.language_service import LanguageService
from services.memory_service import MemoryService
from services.query_service import rewrite_question
from services.document_manager import DocumentManager
from ui.styles import load_css
from ui.header import show_header
from ui.sidebar import show_sidebar
from ui.chat import user_message, assistant_message
from ui.source_card import show_sources
from ui.features import show_features
from ui.document_list import show_documents
st.set_page_config(
    page_title="EduBot AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)
load_css()
show_header()

# Load local .env (for local development)
load_dotenv()

# Get API key
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
else:
    api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")
rag = RAGService()
language = LanguageService()
memory = MemoryService()
document_manager = DocumentManager()

pdf_text = ""
documents = []
chunks = []
embeddings = None
index = None
# Sidebar
uploaded_files = show_sidebar(chunks)
page_count = 0
if uploaded_files:

    show_documents(uploaded_files)
    data = document_manager.process_documents(
        uploaded_files,
        rag
    )

    if data is None:

        st.error("❌ No readable text found.")

        st.stop()

    pdf_text = data["pdf_text"]
    chunks = data["chunks"]
    metadata = data["metadata"]
    embeddings = data["embeddings"]
    index = data["index"]

    page_count = len(data["metadata"])

# left, right = st.columns([4, 1], gap="large")
    with st.expander("📄 View Extracted Text"):

        st.text_area(
            "",
            pdf_text[:2000],
            height=300
        )

    if st.button("✨ Generate AI Summary"):

        with st.spinner("Generating Summary..."):

            summary = generate_summary(
                model,
                pdf_text
            )

            st.subheader("📚 PDF Summary")

            st.write(summary)

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_sessions" not in st.session_state:
    st.session_state.chat_sessions = []

# Display Old Messages
for i, message in enumerate(st.session_state.messages):

    if message["role"] == "user":

        user_message(message["content"])

    else:

        assistant_message(message["content"])

# Chat Input
question = st.chat_input("💬 Ask an Educational Question ...")

if question and question.strip():

    # Show User Message
    user_message(question)
    # Save User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Education Check

    # Detect follow-up questions
    followup_words = [
        "it",
        "this",
        "that",
        "these",
        "those",
        "them",
        "its",

        "explain",
        "again",
        "continue",
        "more",
        "next",
        "summary",
        "summarize",
        "example",
        "why",
        "how"
]

    is_followup = (
        len(st.session_state.messages) > 1
        and any(
            word in question.lower()
            for word in followup_words
        )
    )   

# Only classify NEW questions
    if not uploaded_files:

        if not is_followup:

            if not is_education_question(question, model):

                bot_reply = "❌ Sorry, I can only answer educational questions."

                assistant_message(bot_reply)
                
                st.session_state.messages.append(
                {
                        "role": "assistant",
                        "content": bot_reply
                }
            )

                st.stop()

# Continue with AI Response
    with st.spinner("🧠 EduBot is analyzing ..."):
            
     if uploaded_files:

         selected_language = st.session_state.get(
             "response_language",
             "Auto"
)

         if selected_language == "Auto":

             response_language = language.detect_language(question)

         else:

             response_language = selected_language

         # Use previous question for follow-up retrieval
         chat_history = memory.build_chat_history(
             st.session_state.messages
)

         if is_followup:

             search_question = rewrite_question(
                 model,
                 chat_history,
                 question
    )
         else:

             search_question = question

         results = rag.search(
             search_question,
             chunks,
             metadata,
             embeddings,
             index
    )

         if len(results) == 0:

             bot_reply = (
                 "❌ Sorry, I couldn't find any relevant information "
                 "in the uploaded document(s)."
        )

             references = []

         else:

             context = "\n\n".join(
                 result["text"]
                 for result in results
        )

             references = list(
                 set(
                     f"{result['source']} (Page {result['page']})"
                     for result in results
            )
        )

             chat_history = memory.build_chat_history(
                 st.session_state.messages
        )

             bot_reply = generate_answer(
                 model,
                 context,
                 search_question,
                 response_language,
                 chat_history
        )

     else:

         response = model.generate_content(question)
         bot_reply = response.text

     assistant_message(bot_reply)
    #  chat_actions(
        #  bot_reply,
        #  len(st.session_state.messages)
    #  )

     if uploaded_files and references:
         show_sources(sorted(references))
# ALWAYS display the answer
    st.session_state.messages.append(
    {
            "role": "assistant",
            "content": bot_reply
    }
)
        