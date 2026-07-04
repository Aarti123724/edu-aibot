import streamlit as st


def info_card(title, value, icon):

    st.markdown(
        f"""
<div style="
background:linear-gradient(145deg,#1E293B,#111827);
padding:32px;
border-radius:22px;
border:1px solid #334155;
box-shadow:0px 15px 35px rgba(37,99,235,.25);
text-align:center;
margin-bottom:18px;
">

<div style="
font-size:40px;
margin-bottom:12px;">
{icon}
</div>

<div style="
font-size:15px;
color:#94A3B8;">
{title}
</div>

<div style="
font-size:42px;
font-weight:700;
color:white;
margin-top:8px;">
{value}
</div>

</div>
""",
        unsafe_allow_html=True,
    )