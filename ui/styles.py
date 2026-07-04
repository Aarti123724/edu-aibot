import streamlit as st


def load_css():
    st.markdown("""
<style>

/* =========================
   Global
========================= */

.stApp{
    background:#0F172A;
    color:white;
}

.block-container{
    max-width:1450px;
    padding-top:1.5rem;
    padding-left:2rem;
    padding-right:2rem;
}

/* =========================
   Sidebar
========================= */

section[data-testid="stSidebar"]{
    background:#111827;
    border-right:1px solid #1F2937;
}

/* =========================
   Text
========================= */

h1,h2,h3,h4,h5{
    color:white;
    font-weight:700;
}

p,label,span{
    color:#E5E7EB;
}

/* =========================
   Buttons
========================= */

.stButton > button{

    width:100%;
    height:48px;

    border-radius:12px;

    border:none;

    background:#2563EB;

    color:white;

    font-weight:600;
}

.stButton > button:hover{

    background:#1D4ED8;

}

/* =========================
   File Uploader
========================= */

[data-testid="stFileUploader"]{

    background:#1E293B;

    border:2px dashed #3B82F6;

    border-radius:16px;

    padding:18px;

}

/* =========================
   Hero
========================= */

.hero{

    background:linear-gradient(
        135deg,
        #1E3A8A,
        #172554
    );

    padding:30px 35px;

    border-radius:20px;

    border:1px solid #334155;

    margin-bottom:25px;

}

.hero-title{

    font-size:48px;

    font-weight:800;

    color:white;

}

.hero-subtitle{

    margin-top:6px;

    font-size:22px;

    color:#E2E8F0;

}

.hero-description{

    margin-top:12px;

    font-size:16px;

    color:#CBD5E1;

    line-height:1.7;

}

/* =========================
   Dashboard Cards
========================= */

.info-card{

    background:#1E293B;

    border:1px solid #334155;

    border-radius:18px;

    padding:24px;

    text-align:center;

    min-height:180px;

    transition:.25s;

}

.info-card:hover{

    transform:translateY(-5px);

    border-color:#3B82F6;

    box-shadow:0 10px 30px rgba(37,99,235,.20);

}

.card-icon{

    font-size:38px;

}

.card-title{

    margin-top:14px;

    color:#94A3B8;

    font-size:16px;

}

.card-value{

    margin-top:15px;

    font-size:42px;

    font-weight:700;

    color:white;

}

/* =========================
   Chat
========================= */

.user-message{

    background:#2563EB;

    color:white;

    padding:16px 20px;

    border-radius:18px;

    margin:14px 0 14px auto;

    max-width:75%;

    width:fit-content;

    box-shadow:0 4px 15px rgba(0,0,0,.20);

}
.assistant-message{

    background:#1E293B;

    color:white;

    padding:16px 20px;

    border-radius:18px;

    margin:14px auto 14px 0;

    max-width:75%;

    width:fit-content;

    border:1px solid #334155;

    box-shadow:0 4px 15px rgba(0,0,0,.15);

}

/* =========================
   Source Card
========================= */

.source-card{

    background:#172554;

    border-left:5px solid #3B82F6;

    border-radius:12px;

    padding:16px;

    margin-bottom:10px;

    color:white;

}

/* =========================
   Expander
========================= */

.streamlit-expanderHeader{

    font-weight:600;

}

/* =========================
   Divider
========================= */

hr{

    border-color:#334155;

}

</style>
""", unsafe_allow_html=True)