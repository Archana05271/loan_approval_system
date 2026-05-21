import streamlit as st

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="LoanSmart | Home",
    page_icon="🏦",
    layout="wide"
)

# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

/* GOOGLE FONT */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* MAIN BACKGROUND */

.stApp{
    background: linear-gradient(135deg,#f8f4fb,#efe6f5,#ffffff);
}

/* REMOVE EXTRA SPACE */

.block-container{
    padding-top:1rem;
    padding-left:2rem;
    padding-right:2rem;
    padding-bottom:2rem;
}

/* HEADER */

[data-testid="stHeader"]{
    background:transparent;
}

/* SIDEBAR */

[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#5b1e5c,#7b2d7d);
}

[data-testid="stSidebar"] *{
    color:white !important;
}

/* HERO SECTION */

.hero{
    background: linear-gradient(135deg,#5b1e5c,#8d44ad);
    padding:60px 30px;
    border-radius:25px;
    text-align:center;
    color:white;
    margin-bottom:30px;
    box-shadow:0px 10px 30px rgba(91,30,92,0.25);
}

/* TITLE */

.title{
    font-size:58px;
    font-weight:800;
    margin-bottom:10px;
}

/* SUBTITLE */

.subtitle{
    font-size:22px;
    color:#f3e8ff;
    margin-bottom:20px;
}

/* BADGES */

.badge-row{
    display:flex;
    justify-content:center;
    gap:12px;
    flex-wrap:wrap;
}

.badge{
    background:rgba(255,255,255,0.15);
    padding:10px 20px;
    border-radius:30px;
    font-size:13px;
    font-weight:600;
    border:1px solid rgba(255,255,255,0.2);
}

/* FEATURE CARDS */

.card{
    background:white;
    border-radius:22px;
    padding:30px;
    min-height:240px;
    box-shadow:0px 8px 25px rgba(0,0,0,0.08);
    transition:0.4s;
    margin-bottom:20px;
}

.card:hover{
    transform:translateY(-10px);
    box-shadow:0px 12px 30px rgba(91,30,92,0.18);
}

.card h2{
    color:#5b1e5c !important;
    font-size:28px;
    margin-bottom:15px;
}

.card p{
    color:#555;
    line-height:1.8;
    font-size:15px;
}

/* STATS */

.stat-row{
    display:flex;
    justify-content:center;
    gap:35px;
    flex-wrap:wrap;
    margin:40px 0;
}

.stat-box{
    background:white;
    padding:25px 35px;
    border-radius:20px;
    text-align:center;
    box-shadow:0px 5px 18px rgba(0,0,0,0.07);
    min-width:180px;
    transition:0.3s;
}

.stat-box:hover{
    transform:translateY(-5px);
}

.stat-number{
    font-size:38px;
    font-weight:800;
    color:#5b1e5c;
}

.stat-label{
    color:#777;
    margin-top:5px;
}

/* SECTION TITLE */

.section-title{
    text-align:center;
    font-size:34px;
    font-weight:800;
    color:#5b1e5c;
    margin:40px 0 25px 0;
}

/* STEP CARDS */

.step-card{
    background:white;
    border-radius:22px;
    padding:28px;
    text-align:center;
    min-height:220px;
    box-shadow:0px 5px 18px rgba(0,0,0,0.07);
    transition:0.4s;
}

.step-card:hover{
    transform:translateY(-8px);
    box-shadow:0px 10px 25px rgba(91,30,92,0.15);
}

.step-title{
    color:#5b1e5c;
    font-size:22px;
    font-weight:700;
    margin-top:12px;
}

.step-text{
    color:#666;
    margin-top:10px;
    line-height:1.6;
}

/* FOOTER */

.footer{
    text-align:center;
    color:#777;
    font-size:14px;
    margin-top:50px;
    padding:20px;
}

/* BUTTON */

.stButton>button{
    background:linear-gradient(135deg,#5b1e5c,#8d44ad);
    color:white;
    border:none;
    border-radius:12px;
    padding:12px 28px;
    font-weight:600;
    transition:0.3s;
}

.stButton>button:hover{
    transform:scale(1.05);
    box-shadow:0px 5px 18px rgba(91,30,92,0.25);
}

/* ANIMATION */

.card, .step-card, .stat-box{
    animation:fadeInUp 0.8s ease;
}

@keyframes fadeInUp{
    from{
        opacity:0;
        transform:translateY(25px);
    }
    to{
        opacity:1;
        transform:translateY(0px);
    }
}

</style>
""", unsafe_allow_html=True)

# =========================================
# HERO SECTION
# =========================================

st.markdown("""
<div class='hero'>

<div class='title'>
🏦 LoanSmart
</div>

<div class='subtitle'>
AI-Powered Loan Approval Prediction Platform
</div>

<div class='badge-row'>
    <div class='badge'>✅ 80% Accuracy</div>
    <div class='badge'>⚡ Instant Results</div>
    <div class='badge'>🔒 Secure System</div>
    <div class='badge'>📊 Smart Analytics</div>
</div>

</div>
""", unsafe_allow_html=True)

# =========================================
# HERO IMAGE
# =========================================

image_url = "https://images.unsplash.com/photo-1520607162513-77705c0f0d4a"

st.image(image_url, width=1200)

# =========================================
# STATS
# =========================================

st.markdown("""
<div class='stat-row'>

<div class='stat-box'>
    <div class='stat-number'>4K+</div>
    <div class='stat-label'>Applications</div>
</div>

<div class='stat-box'>
    <div class='stat-number'>80%</div>
    <div class='stat-label'>Accuracy</div>
</div>

<div class='stat-box'>
    <div class='stat-number'>3s</div>
    <div class='stat-label'>Prediction Time</div>
</div>

<div class='stat-box'>
    <div class='stat-number'>8+</div>
    <div class='stat-label'>Risk Factors</div>
</div>

</div>
""", unsafe_allow_html=True)

# =========================================
# FEATURE CARDS
# =========================================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
<div class='card'>
    <h2>📊 Smart Dashboard</h2>
    <p>
    Analyze loan trends, approvals,
    applicant details, and financial
    reports using interactive charts
    and visual analytics.
    </p>
</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class='card'>
    <h2>🤖 AI Prediction</h2>
    <p>
    Predict loan approval instantly
    using Machine Learning algorithms
    trained on applicant financial data
    and credit history.
    </p>
</div>
""", unsafe_allow_html=True)

with col3:
    st.markdown("""
<div class='card'>
    <h2>📋 Risk Analysis</h2>
    <p>
    Understand rejection reasons,
    low credit risk factors,
    income limitations,
    and approval insights.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================================
# HOW IT WORKS
# =========================================

st.markdown("""
<div class='section-title'>
🔍 How It Works
</div>
""", unsafe_allow_html=True)

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.markdown("""
<div class='step-card'>
    <div style='font-size:36px;'>1️⃣</div>
    <div class='step-title'>Enter Details</div>
    <div class='step-text'>
    Fill applicant financial and personal details.
    </div>
</div>
""", unsafe_allow_html=True)

with s2:
    st.markdown("""
<div class='step-card'>
    <div style='font-size:36px;'>2️⃣</div>
    <div class='step-title'>AI Analysis</div>
    <div class='step-text'>
    Machine Learning model evaluates risk factors.
    </div>
</div>
""", unsafe_allow_html=True)

with s3:
    st.markdown("""
<div class='step-card'>
    <div style='font-size:36px;'>3️⃣</div>
    <div class='step-title'>Get Prediction</div>
    <div class='step-text'>
    Instantly receive loan approval prediction.
    </div>
</div>
""", unsafe_allow_html=True)

with s4:
    st.markdown("""
<div class='step-card'>
    <div style='font-size:36px;'>4️⃣</div>
    <div class='step-title'>View Insights</div>
    <div class='step-text'>
    Understand approval or rejection reasons clearly.
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================
# CTA SECTION
# =========================================

st.markdown("""
<div class='section-title'>
🚀 Start Your Smart Loan Analysis
</div>
""", unsafe_allow_html=True)

st.write("")

center1, center2, center3 = st.columns([1,2,1])

with center2:
    st.button("🔍 Predict Loan Approval")

# =========================================
# FOOTER
# =========================================

st.markdown("""
<div class='footer'>
🏦 LoanSmart · Machine Learning Loan Prediction System · Developed by Archana
</div>
""", unsafe_allow_html=True)