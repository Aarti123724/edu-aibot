import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai

from classifier import is_education_question
from pdf_utils import extract_pdf_text
from rag_utils import (
    split_text,
    create_embeddings,
    create_faiss_index,
    search_chunks
)
# from ocr_utils import extract_text_from_scanned_pdf
from gemini_ocr import extract_text_with_gemini

# Load environment variables
load_dotenv()

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

# Page Title
st.title("🎓 EduBot")
st.subheader("Educational AI Assistant")

# PDF Upload
uploaded_file = st.file_uploader(
    "📄 Upload PDF",
    type=["pdf"]
)

pdf_text = ""
chunks = []
embeddings = None
index = None

if uploaded_file:

    pdf_text = extract_pdf_text(uploaded_file)
    # st.write("PDF Text Length:", len(pdf_text))

    if not pdf_text.strip():

        st.error(
        "This PDF contains scanned images. Please upload a text-based PDF."
    )

        st.stop()

        # st.write("OCR Text Length:", len(pdf_text))
    # RAG Processing
    chunks = split_text(pdf_text)

    # st.write("Total Chunks:", len(chunks))

    if len(chunks) == 0:
     st.error("❌ No text extracted from PDF")
     st.stop()

    embeddings = create_embeddings(chunks)

    # st.write("Embedding Shape:", embeddings.shape)

    index = create_faiss_index(
    embeddings
    )

    # st.write("FAISS Index Size:", index.ntotal)

    with st.expander("📄 View Extracted Text"):
     st.text_area(
        "",
        pdf_text[:2000],
        height=300
    )

    if st.button("📄 Summarize PDF"):

        with st.spinner("Generating Summary..."):

            summary_prompt = f"""
            Summarize the following educational document.

            Give:

            1. Main Topics
            2. Key Concepts
            3. Important Points
            4. Short Summary

            Document:

            {pdf_text[:10000]}
            """

            summary = model.generate_content(
                summary_prompt
            )

            st.subheader("📚 PDF Summary")

            st.write(summary.text)

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Old Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
# Clear Chat Button
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Chat Input
question = st.chat_input("Ask an Educational Question")

if question and question.strip():

    # Show User Message
    st.chat_message("user").markdown(question)

    # Save User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Education Check
    if not is_education_question(question, model):

        bot_reply = "❌ Sorry, I can only answer educational questions."

        st.chat_message("assistant").markdown(bot_reply)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": bot_reply
            }
        )

    
    else:

        with st.spinner("Thinking..."):

            if uploaded_file:

                relevant_chunks = search_chunks(
                    question,
                    chunks,
                    embeddings,
                    index
                )

                context = "\n\n".join(
                    relevant_chunks
                )

                prompt = f"""
                You are an educational assistant.

                Use ONLY the provided context
                to answer the question.

                If the answer is not available
                in the context, reply:

                "The answer is not available in the uploaded document."

                Context:

                {context}

                Question:

                {question}
                """

                response = model.generate_content(
                    prompt
                )

            else:

                response = model.generate_content(
                    question
                )

            bot_reply = response.text

            st.chat_message("assistant").markdown(
                bot_reply
            )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": bot_reply
                }
            )
        