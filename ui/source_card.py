import streamlit as st


def show_sources(references):

    if not references:
        return

    st.markdown("### 📄 Sources")

    for reference in references:

        st.markdown(
            f"""
<div class="source-card">

📄 {reference}

</div>
""",
            unsafe_allow_html=True
        )