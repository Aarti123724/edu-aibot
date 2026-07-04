import streamlit as st


def show_documents(uploaded_files):

    if not uploaded_files:
        return

    st.markdown("## 📚 Uploaded Documents")

    for pdf in uploaded_files:

        st.markdown(
            f"""
<div style="
background:#1E293B;
padding:15px;
border-radius:12px;
border:1px solid #334155;
margin-bottom:12px;
">

<b>📄 {pdf.name}</b>

<br>

<span style="color:#22C55E;">
✓ Ready
</span>

</div>
""",
            unsafe_allow_html=True
        )