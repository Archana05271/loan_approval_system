import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Loan Prediction System",
    page_icon="🏦",
    layout="wide"
)

# =====================================================
# ENHANCED CSS
# =====================================================

st.markdown("""
<style>

/* IMPORT FONT */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght=300;400;500;600;700;800&display=swap');

/* GLOBAL FONT */
html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Poppins', sans-serif;
}

/* MAIN BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #f8f5fb, #f3edf7, #ffffff);
}

/* REMOVE WHITE SPACE */
.block-container {
    padding-top: 1rem;
    padding-left: 2rem;
    padding-right: 2rem;
    padding-bottom: 2rem;
}

/* HEADER */
[data-testid="stHeader"] {
    background: transparent;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #5b1e5c, #7b2d7d);
}

[data-testid="stSidebar"] * {
    color: white !important;
}

/* TITLE */
.main-title {
    text-align: center;
    font-size: 65px;
    font-weight: 800;
    color: #5b1e5c;
    margin-bottom: 5px;
    animation: fadeDown 1s ease;
}

/* SUB TITLE */
.sub-title {
    text-align: center;
    color: #666;
    font-size: 22px;
    margin-bottom: 18px;
}

/* BADGES */
.badge-row {
    display: flex;
    justify-content: center;
    gap: 12px;
    flex-wrap: wrap;
    margin-bottom: 30px;
}

.badge {
    background: white;
    padding: 10px 18px;
    border-radius: 30px;
    color: #5b1e5c;
    font-size: 14px;
    font-weight: 700;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
}

/* HERO IMAGE STYLING */
[data-testid="stImage"] img {
    border-radius: 25px !important;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.10) !important;
}

/* CARD */
.card {
    background: rgba(255,255,255,0.95);
    border-radius: 24px;
    padding: 30px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.08);
    min-height: 240px;
    transition: 0.4s ease;
    border-top: 5px solid #5b1e5c;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0px 12px 28px rgba(91,30,92,0.15);
}

/* FIX TEXT */
.card h2 {
    color: #5b1e5c !important;
    font-size: 30px;
    margin-bottom: 15px;
}

.card p {
    color: #555 !important;
    font-size: 17px;
    line-height: 1.8;
}

/* STATS SECTION */
.stats-row {
    display: flex;
    justify-content: center;
    gap: 50px;
    flex-wrap: wrap;
    margin-top: 35px;
    margin-bottom: 35px;
}

.stat-box {
    text-align: center;
}

.stat-number {
    font-size: 38px;
    font-weight: 800;
    color: #5b1e5c;
}

.stat-label {
    color: #777;
    font-size: 15px;
}

/* HOW IT WORKS */
.section-title {
    text-align: center;
    font-size: 36px;
    color: #5b1e5c;
    font-weight: 800;
    margin-top: 20px;
    margin-bottom: 25px;
}

.step-card {
    background: white;
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    min-height: 210px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.06);
    transition: 0.3s ease;
}

.step-card:hover {
    transform: translateY(-6px);
}

.step-title {
    color: #5b1e5c;
    font-size: 22px;
    font-weight: 700;
    margin-top: 12px;
}

.step-text {
    color: #666;
    font-size: 15px;
    margin-top: 10px;
    line-height: 1.7;
}

/* SUCCESS ALERT */
div[data-testid="stNotification"] {
    background-color: rgba(91, 30, 92, 0.08) !important;
    border: 1px solid #5b1e5c !important;
    border-radius: 14px !important;
}

div[data-testid="stNotification"] p {
    color: #4a124b !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}

/* FOOTER */
.footer {
    text-align: center;
    color: #888;
    font-size: 14px;
    margin-top: 40px;
    padding-bottom: 20px;
}

/* ANIMATIONS */
@keyframes fadeDown {
    from {
        opacity: 0;
        transform: translateY(-25px);
    }
    to {
        opacity: 1;
        transform: translateY(0px);
    }
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# TITLE
# =====================================================

st.markdown("""
<div class='main-title'>
🏦 Loan Approval Prediction System
</div>

<div class='sub-title'>
AI Powered Banking Platform with Smart Financial Intelligence
</div>

<div class='badge-row'>
    <div class='badge'>🤖 Machine Learning</div>
    <div class='badge'>📊 Analytics Dashboard</div>
    <div class='badge'>⚡ Instant Prediction</div>
    <div class='badge'>🔒 Secure System</div>
</div>
""", unsafe_allow_html=True)

# =====================================================
# HERO IMAGE (FIXED TRAPPING BUG)
# =====================================================

st.image(
    "https://images.unsplash.com/photo-1554224155-6726b3ff858f",
    use_container_width=True
)

# =====================================================
# STATS
# =====================================================

st.markdown("""
<div class='stats-row'>
    <div class='stat-box'>
        <div class='stat-number'>4K+</div>
        <div class='stat-label'>Applications</div>
    </div>
    <div class='stat-box'>
        <div class='stat-number'>80%</div>
        <div class='stat-label'>Prediction Accuracy</div>
    </div>
    <div class='stat-box'>
        <div class='stat-number'>3s</div>
        <div class='stat-label'>Processing Time</div>
    </div>
    <div class='stat-box'>
        <div class='stat-number'>24/7</div>
        <div class='stat-label'>System Availability</div>
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================================
# FEATURE CARDS
# =====================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='card'>
    <h2>📊 Dashboard</h2>
    <p>
    Visualize applicant financial analytics, approval distributions,
    asset evaluations, and interactive loan insights using dynamic charts.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='card'>
    <h2>🤖 AI Prediction</h2>
    <p>
    Predict loan approval instantly using Machine Learning algorithms
    trained on applicant financial and credit history datasets.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='card'>
    <h2>⚡ Fast Results</h2>
    <p>
    Receive quick and intelligent loan approval insights with
    real-time risk assessment and financial analysis.
    </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# HOW IT WORKS
# =====================================================

st.markdown("""
<div class='section-title'>
🔍 How The System Works
</div>
""", unsafe_allow_html=True)

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.markdown("""
    <div class='step-card'>
    <div style='font-size:38px;'>1️⃣</div>
    <div class='step-title'>Enter Details</div>
    <div class='step-text'>Fill applicant financial and personal details.</div>
    </div>
    """, unsafe_allow_html=True)

with s2:
    st.markdown("""
    <div class='step-card'>
    <div style='font-size:38px;'>2️⃣</div>
    <div class='step-title'>Data Processing</div>
    <div class='step-text'>System scales and processes financial information.</div>
    </div>
    """, unsafe_allow_html=True)

with s3:
    st.markdown("""
    <div class='step-card'>
    <div style='font-size:38px;'>3️⃣</div>
    <div class='step-title'>AI Prediction</div>
    <div class='step-text'>ML model evaluates approval probability and risk.</div>
    </div>
    """, unsafe_allow_html=True)

with s4:
    st.markdown("""
    <div class='step-card'>
    <div style='font-size:38px;'>4️⃣</div>
    <div class='step-title'>Get Result</div>
    <div class='step-text'>View approval result and financial insights instantly.</div>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# SUCCESS STATUS
# =====================================================

st.success("✅ Navigate through the sidebar to explore prediction, dashboard analytics, and project insights.")

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class='footer'>
🏦 LoanSmart · AI Loan Prediction Platform · Developed by Archana
</div>
""", unsafe_allow_html=True)