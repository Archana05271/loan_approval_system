import streamlit as st
import numpy as np
import pandas as pd
import joblib
import os

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Loan Prediction",
    page_icon="🏦",
    layout="wide"
)

# =====================================================
# LOAD MODEL & SCALER
# =====================================================

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# =====================================================
# ENHANCED MODERN UI CSS
# =====================================================

st.markdown("""
<style>

/* IMPORT FONT */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

/* GLOBAL FONT */
html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* MAIN BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #f8f5fb, #f2ebf7, #ffffff) !important;
}

/* REMOVE EXTRA SPACING */
.block-container{
    padding-top:1rem !important;
    padding-bottom:2rem !important;
    padding-left:2rem !important;
    padding-right:2rem !important;
}

/* HEADER */
[data-testid="stHeader"]{
    background: transparent !important;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#5b1e5c,#7b2d7d) !important;
    border-right: 2px solid rgba(255,255,255,0.08);
}

/* SIDEBAR TEXT */
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label {
    color: white !important;
}

/* MAIN TITLE */
.title {
    text-align: center;
    font-size: 58px;
    font-weight: 800;
    color: #5b1e5c;
    margin-bottom: 10px;
    animation: fadeInDown 1s ease;
}

/* SUBTITLE */
.subtitle{
    text-align:center;
    color:#666666;
    font-size:20px;
    margin-bottom:30px;
    animation: fadeIn 1.2s ease;
}

/* TOP INFO BADGES */
.badge-row{
    display:flex;
    justify-content:center;
    gap:12px;
    flex-wrap:wrap;
    margin-bottom:30px;
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

/* FORM CONTAINER */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,255,255,0.92) !important;
    padding: 30px !important;
    border-radius: 24px !important;
    box-shadow: 0px 8px 28px rgba(0,0,0,0.08) !important;
    border: 1px solid rgba(255,255,255,0.4);
    backdrop-filter: blur(8px);
    animation: fadeInUp 0.8s ease;
}

/* LABELS */
div[data-testid="stVerticalBlockBorderWrapper"] label p {
    color: #222222 !important;
    font-weight: 600 !important;
    font-size: 15px !important;
}

/* INPUT BOXES */
div[data-baseweb="input"],
div[data-baseweb="select"] {
    background-color: #ffffff !important;
    border: 1px solid #dddddd !important;
    border-radius: 12px !important;
    transition: 0.3s ease;
}

/* INPUT HOVER EFFECT */
div[data-baseweb="input"]:hover,
div[data-baseweb="select"]:hover {
    border: 1px solid #8d44ad !important;
    box-shadow: 0px 0px 10px rgba(141,68,173,0.15);
}

/* INPUT TEXT */
input,
div[data-testid="stSelectbox"] div {
    color: #222222 !important;
    -webkit-text-fill-color: #222222 !important;
}

/* BUTTON */
.stButton > button {
    background: linear-gradient(135deg,#5b1e5c,#8d44ad) !important;
    color: white !important;
    border: none !important;
    border-radius: 14px !important;
    height: 55px !important;
    width: 280px !important;
    font-size: 18px !important;
    font-weight: 700 !important;
    transition: 0.3s ease !important;
    box-shadow: 0px 6px 18px rgba(91,30,92,0.25);
}

/* BUTTON HOVER */
.stButton > button:hover {
    transform: translateY(-3px) scale(1.02);
    background: linear-gradient(135deg,#7b2d7d,#a855f7) !important;
    box-shadow: 0px 10px 22px rgba(91,30,92,0.35);
}

/* GIF STYLING */
img {
    border-radius: 20px !important;
}

/* FOOTER */
.footer{
    text-align:center;
    color:#777777;
    font-size:14px;
    margin-top:40px;
    padding:20px;
}

/* ANIMATIONS */
@keyframes fadeInUp{
    from{
        opacity:0;
        transform:translateY(30px);
    }
    to{
        opacity:1;
        transform:translateY(0px);
    }
}

@keyframes fadeInDown{
    from{
        opacity:0;
        transform:translateY(-30px);
    }
    to{
        opacity:1;
        transform:translateY(0px);
    }
}

@keyframes fadeIn{
    from{
        opacity:0;
    }
    to{
        opacity:1;
    }
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# TITLE SECTION
# =====================================================

st.markdown("""
<div class='title'>
🏦 Loan Approval Prediction
</div>

<div class='subtitle'>
AI-Powered Smart Loan Eligibility & Risk Analysis System
</div>

<div class='badge-row'>
    <div class='badge'>✅ AI Prediction</div>
    <div class='badge'>⚡ Instant Results</div>
    <div class='badge'>🔒 Secure Analysis</div>
    <div class='badge'>📊 Risk Evaluation</div>
</div>
""", unsafe_allow_html=True)

# =====================================================
# FORM INTERFACE
# =====================================================

with st.container(border=True):

    col1, col2 = st.columns(2)

    with col1:

        no_of_dependents = st.number_input(
            "👨‍👩‍👧 Dependents",
            0,
            10
        )

        education = st.selectbox(
            "🎓 Education",
            ["Graduate", "Not Graduate"]
        )

        self_employed = st.selectbox(
            "💼 Self Employed",
            ["Yes", "No"]
        )

        income_annum = st.number_input(
            "💰 Annual Income",
            min_value=0.0,
            value=0.0
        )

        loan_amount = st.number_input(
            "🏦 Loan Amount",
            min_value=0.0,
            value=0.0
        )

    with col2:

        loan_term = st.number_input(
            "📅 Loan Term",
            min_value=0.0,
            value=0.0
        )

        cibil_score = st.number_input(
            "📈 CIBIL Score",
            min_value=300.0,
            max_value=900.0,
            value=650.0
        )

        residential_assets_value = st.number_input(
            "🏠 Residential Assets",
            min_value=0.0,
            value=0.0
        )

        commercial_assets_value = st.number_input(
            "🏢 Commercial Assets",
            min_value=0.0,
            value=0.0
        )

        luxury_assets_value = st.number_input(
            "🚘 Luxury Assets",
            min_value=0.0,
            value=0.0
        )

        bank_asset_value = st.number_input(
            "🏛️ Bank Assets",
            min_value=0.0,
            value=0.0
        )

# =====================================================
# ENCODING INPUTS
# =====================================================

edu_enc = 1 if education == "Graduate" else 0
self_enc = 1 if self_employed == "Yes" else 0

# =====================================================
# PREDICTION LOGIC
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

center1, center2, center3 = st.columns([1,2,1])

with center2:
    predict_btn = st.button("🚀 Predict Loan Status")

if predict_btn:

    if income_annum == 0.0 or loan_amount == 0.0 or loan_term == 0.0:
        st.error("⚠️ Please enter valid values for Annual Income, Loan Amount, and Loan Term before predicting!")

    else:

        feature_names = [
            'no_of_dependents', 'education', 'self_employed', 'income_annum',
            'loan_amount', 'loan_term', 'cibil_score', 'residential_assets_value',
            'commercial_assets_value', 'luxury_assets_value', 'bank_asset_value'
        ]

        input_data = pd.DataFrame([[
            no_of_dependents,
            edu_enc,
            self_enc,
            income_annum,
            loan_amount,
            loan_term,
            cibil_score,
            residential_assets_value,
            commercial_assets_value,
            luxury_assets_value,
            bank_asset_value
        ]], columns=feature_names)

        features_scaled = scaler.transform(input_data)
        prediction = model.predict(features_scaled)

        left_space, center_block, right_space = st.columns([1, 2, 1])

        # =====================================================
        # APPROVED
        # =====================================================

        if prediction[0] == 1:

            st.markdown("""
            <div style="
                background:#ecfff3;
                padding:35px;
                border-radius:24px;
                border-left:8px solid #16a34a;
                text-align:center;
                margin:20px auto;
                max-width:800px;
                box-shadow:0px 6px 18px rgba(0,0,0,0.08);
            ">
            <h1 style="color:#16a34a !important; margin:0; font-size:34px;">
            ✅ LOAN APPROVED
            </h1>

            <p style="color:#2b6a3f !important; font-size:18px; margin-top:12px;">
            Congratulations! Your loan application has been approved successfully.
            </p>
            </div>
            """, unsafe_allow_html=True)

            with center_block:
                if os.path.exists("happy_family.gif"):
                    st.image("happy_family.gif", width=650)
                else:
                    st.info("💡 Add happy_family.gif in your project folder.")

        # =====================================================
        # REJECTED
        # =====================================================

        else:

            st.markdown("""
            <div style="
                background:#fff1f1;
                padding:35px;
                border-radius:24px;
                border-left:8px solid #dc2626;
                text-align:center;
                margin:20px auto;
                max-width:800px;
                box-shadow:0px 6px 18px rgba(0,0,0,0.08);
            ">
            <h1 style="color:#dc2626 !important; margin:0; font-size:34px;">
            ❌ LOAN REJECTED
            </h1>

            <p style="color:#7a2222 !important; font-size:18px; margin-top:12px;">
            Sorry! Your loan application has been rejected.
            </p>
            </div>
            """, unsafe_allow_html=True)

            with center_block:
                if os.path.exists("sad_family.gif"):
                    st.image("sad_family.gif", width=650)
                else:
                    st.info("💡 Add sad_family.gif in your project folder.")

            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown("""
            <h2 style='color:#5b1e5c;'>
            📌 Possible Reasons
            </h2>
            """, unsafe_allow_html=True)

            if cibil_score < 650:
                st.warning("⚠️ Low CIBIL Score")

            if income_annum < loan_amount:
                st.warning("⚠️ Income lower than loan amount")

            if bank_asset_value < 50000:
                st.warning("⚠️ Low bank asset value")

            if no_of_dependents > 4:
                st.warning("⚠️ Too many dependents")

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class='footer'>
🏦 LoanSmart · AI Loan Approval Prediction System · Developed by Archana
</div>
""", unsafe_allow_html=True)