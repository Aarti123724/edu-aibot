import streamlit as st


def show_header():

    st.markdown(
        """
<div style="
background:linear-gradient(135deg,#2563EB,#1E3A8A);
padding:10px 20px;
border-radius:15px;
margin-bottom:20px;
margin-top:20px;
box-shadow:0 8px 25px rgba(0,0,0,.20);
">

<div style="
font-size:48px;
font-weight:900;
font-family:'Segoe UI',sans-serif;
color:white;
line-height:1.1;
">

🎓 EduBot AI

</div>

<div style="
font-size:20px;
color:#E0E7FF;
margin-top:8px;
">

AI-Powered Educational Assistant

</div>

<div style="
margin-top:16px;
font-size:16px;
color:#DBEAFE;
">

Learn Smarter • Search Faster • Study Better
</div>

</div>
""",
        unsafe_allow_html=True
    )