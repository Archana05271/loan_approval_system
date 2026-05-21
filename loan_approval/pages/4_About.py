import streamlit as st

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="LoanSmart | About",
    page_icon="ℹ️",
    layout="wide"
)

# =====================================================
# ENHANCED MODERN CSS
# =====================================================

st.markdown("""
<style>

/* GOOGLE FONT */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

/* GLOBAL FONT */
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* MAIN BACKGROUND */
.stApp {
    background: linear-gradient(135deg,#f8f5fb,#f2ebf7,#ffffff);
}

/* REMOVE EXTRA SPACING */
.block-container{
    padding-top:1rem;
    padding-bottom:2rem;
    padding-left:2rem;
    padding-right:2rem;
}

/* HEADER */
[data-testid="stHeader"]{
    background:transparent;
}

/* SIDEBAR */
[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#5b1e5c,#7b2d7d);
    border-right:2px solid rgba(255,255,255,0.08);
}

[data-testid="stSidebar"] *{
    color:white !important;
}

/* MAIN TITLE */
.title{
    text-align:center;
    font-size:58px;
    color:#5b1e5c;
    font-weight:800;
    margin-bottom:8px;
    animation:fadeInDown 1s ease;
}

/* SUBTITLE */
.subtitle{
    text-align:center;
    font-size:18px;
    color:#666666;
    margin-bottom:30px;
}

/* BADGES */
.badge-row{
    display:flex;
    justify-content:center;
    gap:12px;
    flex-wrap:wrap;
    margin-bottom:35px;
}

.badge{
    background:white;
    padding:10px 18px;
    border-radius:30px;
    color:#5b1e5c;
    font-size:14px;
    font-weight:700;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
}

/* HERO CARD */
.hero-card{
    background:rgba(255,255,255,0.92);
    border-radius:28px;
    padding:45px;
    box-shadow:0px 8px 28px rgba(0,0,0,0.08);
    border-left:8px solid #5b1e5c;
    margin-bottom:35px;
    animation:fadeInUp 1s ease;
}

.hero-card h2{
    color:#5b1e5c !important;
    margin-top:0;
    font-size:34px;
    font-weight:800;
    margin-bottom:18px;
}

.hero-card p{
    color:#444444 !important;
    font-size:17px;
    line-height:1.9;
}

/* SECTION TITLE */
.section-title{
    font-size:30px;
    color:#5b1e5c;
    font-weight:800;
    margin-top:25px;
    margin-bottom:20px;
}

/* FEATURE CARDS */
.grid-box{
    background:rgba(255,255,255,0.95);
    padding:28px;
    border-radius:22px;
    box-shadow:0px 6px 20px rgba(0,0,0,0.06);
    transition:0.4s ease;
    min-height:220px;
    animation:fadeInUp 1s ease;
}

.grid-box:hover{
    transform:translateY(-8px);
    box-shadow:0px 12px 28px rgba(91,30,92,0.15);
}

.grid-box h4{
    color:#5b1e5c !important;
    margin-top:0;
    font-size:22px;
    font-weight:700;
    margin-bottom:14px;
}

.grid-box p{
    color:#666666 !important;
    font-size:15px;
    line-height:1.8;
}

/* STACK CONTAINER */
.stack-container{
    background:rgba(255,255,255,0.95);
    padding:35px 25px;
    border-radius:24px;
    box-shadow:0px 6px 22px rgba(0,0,0,0.06);
    text-align:center;
    animation:fadeInUp 1s ease;
}

/* TECH BADGES */
.tech-badge{
    display:inline-block;
    background:linear-gradient(135deg,#ede3ef,#f7f1f9);
    color:#5b1e5c !important;
    padding:12px 18px;
    border-radius:30px;
    font-weight:700;
    font-size:14px;
    margin:8px;
    box-shadow:0px 3px 10px rgba(91,30,92,0.08);
    transition:0.3s ease;
}

.tech-badge:hover{
    transform:scale(1.05);
}

/* AUTHOR CARD */
.author-card{
    background:linear-gradient(135deg,#1f1f2f,#2d2d44);
    padding:35px;
    border-radius:24px;
    text-align:center;
    margin-top:45px;
    box-shadow:0px 8px 24px rgba(0,0,0,0.15);
    animation:fadeInUp 1s ease;
}

.author-card h3{
    color:#d5b4d7 !important;
    margin:0 0 8px 0;
    font-size:14px;
    letter-spacing:3px;
    text-transform:uppercase;
}

.author-card p{
    color:#ffffff !important;
    font-size:34px;
    font-weight:800;
    margin:0;
}

/* FOOTER */
.footer{
    text-align:center;
    color:#888888;
    font-size:14px;
    margin-top:35px;
    padding:18px;
}

/* ANIMATIONS */
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

@keyframes fadeInDown{
    from{
        opacity:0;
        transform:translateY(-25px);
    }
    to{
        opacity:1;
        transform:translateY(0px);
    }
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER SECTION
# =====================================================

st.markdown("""
<div class='title'>
ℹ️ About Project
</div>

<div class='subtitle'>
System Architecture Framework Overview & Smart Loan Intelligence Platform
</div>

<div class='badge-row'>
    <div class='badge'>🤖 AI Powered</div>
    <div class='badge'>📊 Analytics Dashboard</div>
    <div class='badge'>🔒 Secure System</div>
    <div class='badge'>⚡ Real-Time Prediction</div>
</div>
""", unsafe_allow_html=True)

# =====================================================
# HERO SECTION
# =====================================================

st.markdown("""
<div class='hero-card'>

<h2>
🏦 Intelligent Loan Evaluation Engine
</h2>

<p>
LoanSmart is an end-to-end AI-powered financial intelligence platform developed to modernize and simplify the traditional loan approval process. The system leverages Machine Learning algorithms to analyze applicant financial records, evaluate risk factors, inspect credit behavior, and generate instant loan eligibility predictions with high accuracy.
<br><br>
The platform combines predictive analytics, interactive dashboards, risk evaluation modules, and smart visualization tools to help financial institutions process loan applications faster and more efficiently while reducing manual verification complexity.
</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# CORE FEATURES
# =====================================================

st.markdown("""
<div class='section-title'>
📌 System Core Capabilities
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class='grid-box'>

    <h4>
    🔮 Real-Time Inference
    </h4>

    <p>
    Instantly processes applicant financial attributes and predicts loan approval outcomes using trained Machine Learning models.
    </p>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class='grid-box'>

    <h4>
    📊 Interactive Analytics
    </h4>

    <p>
    Visualizes loan trends, approval distributions, income patterns, and financial metrics through interactive Plotly charts.
    </p>

    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class='grid-box'>

    <h4>
    🔒 Secure Architecture
    </h4>

    <p>
    Implements structured data handling, isolated model loading, and efficient system workflow management for safe predictions.
    </p>

    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# TECHNOLOGY STACK
# =====================================================

st.markdown("""
<div class='section-title'>
🚀 Technology Stack
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='stack-container'>

<span class='tech-badge'>🐍 Python 3.x</span>

<span class='tech-badge'>⚡ Streamlit Framework</span>

<span class='tech-badge'>🤖 Scikit-Learn ML Model</span>

<span class='tech-badge'>🐼 Pandas Data Processing</span>

<span class='tech-badge'>🔢 NumPy Computation</span>

<span class='tech-badge'>📈 Plotly Visual Analytics</span>

<span class='tech-badge'>📦 Joblib Serialization</span>

<span class='tech-badge'>🎨 HTML + CSS Styling</span>

</div>
""", unsafe_allow_html=True)

# =====================================================
# SYSTEM WORKFLOW
# =====================================================

st.markdown("""
<div class='section-title'>
⚙️ System Workflow
</div>
""", unsafe_allow_html=True)

w1, w2, w3, w4 = st.columns(4)

with w1:

    st.markdown("""
    <div class='grid-box'>

    <h4>1️⃣ Data Input</h4>

    <p>
    User enters applicant financial details and asset information.
    </p>

    </div>
    """, unsafe_allow_html=True)

with w2:

    st.markdown("""
    <div class='grid-box'>

    <h4>2️⃣ Data Processing</h4>

    <p>
    Features are encoded, cleaned, scaled, and prepared for prediction.
    </p>

    </div>
    """, unsafe_allow_html=True)

with w3:

    st.markdown("""
    <div class='grid-box'>

    <h4>3️⃣ ML Prediction</h4>

    <p>
    Machine Learning model analyzes financial risk and predicts loan status.
    </p>

    </div>
    """, unsafe_allow_html=True)

with w4:

    st.markdown("""
    <div class='grid-box'>

    <h4>4️⃣ Smart Insights</h4>

    <p>
    Users receive approval results with intelligent financial analysis insights.
    </p>

    </div>
    """, unsafe_allow_html=True)

# =====================================================
# AUTHOR CARD
# =====================================================

st.markdown("""
<div class='author-card'>

<h3>
Lead Platform Architect
</h3>

<p>
✨ Archana ✨
</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class='footer'>

🏦 LoanSmart · AI Loan Approval Prediction System · Developed using Streamlit & Machine Learning

</div>
""", unsafe_allow_html=True)