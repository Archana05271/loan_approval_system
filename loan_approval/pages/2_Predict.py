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
# BASE DIRECTORY
# =====================================================

BASE_DIR = os.path.dirname(__file__)

# =====================================================
# LOAD MODEL & SCALER
# =====================================================

MODEL_PATH = os.path.join(BASE_DIR, "..", "model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "..", "scaler.pkl")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# =====================================================
# GIF PATHS
# =====================================================

happy_gif = os.path.join(BASE_DIR, "..", "happy_family.gif")
sad_gif = os.path.join(BASE_DIR, "..", "sad_family.gif")

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

/* IMPORT FONT */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* MAIN BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #f8f5fb, #f2ebf7, #ffffff);
}

/* REMOVE EXTRA SPACE */
.block-container{
    padding-top:1rem;
    padding-bottom:2rem;
    padding-left:2rem;
    padding-right:2rem;
}

/* HEADER */
[data-testid="stHeader"]{
    background: transparent;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#5b1e5c,#7b2d7d);
}

[data-testid="stSidebar"] * {
    color:white !important;
}

/* TITLE */
.title {
    text-align:center;
    font-size:55px;
    font-weight:800;
    color:#5b1e5c;
    margin-bottom:10px;
}

/* SUBTITLE */
.subtitle{
    text-align:center;
    color:#666;
    font-size:20px;
    margin-bottom:25px;
}

/* BADGES */
.badge-row{
    display:flex;
    justify-content:center;
    gap:12px;
    flex-wrap:wrap;
    margin-bottom:25px;
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
    background: rgba(255,255,255,0.95) !important;
    padding: 30px !important;
    border-radius: 24px !important;
    box-shadow: 0px 8px 28px rgba(0,0,0,0.08) !important;
    border:none !important;
}

/* LABELS */
label p{
    color:#222 !important;
    font-weight:600 !important;
}

/* INPUTS */
div[data-baseweb="input"],
div[data-baseweb="select"]{
    border-radius:12px !important;
}

/* BUTTON */
.stButton > button{
    background:linear-gradient(135deg,#5b1e5c,#8d44ad);
    color:white;
    border:none;
    border-radius:14px;
    height:55px;
    width:280px;
    font-size:18px;
    font-weight:700;
    box-shadow:0px 6px 18px rgba(91,30,92,0.25);
}

.stButton > button:hover{
    background:linear-gradient(135deg,#7b2d7d,#a855f7);
}

/* FOOTER */
.footer{
    text-align:center;
    color:#777;
    font-size:14px;
    margin-top:40px;
    padding:20px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# TITLE
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
    <div class='badge'>📊 Risk Analysis</div>
    <div class='badge'>🔒 Secure System</div>
</div>
""", unsafe_allow_html=True)

# =====================================================
# FORM
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
# ENCODING
# =====================================================

edu_enc = 1 if education == "Graduate" else 0
self_enc = 1 if self_employed == "Yes" else 0

# =====================================================
# PREDICT BUTTON
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

center1, center2, center3 = st.columns([1,2,1])

with center2:
    predict_btn = st.button("🚀 Predict Loan Status")

# =====================================================
# PREDICTION
# =====================================================

if predict_btn:

    if income_annum == 0 or loan_amount == 0 or loan_term == 0:
        st.error("⚠️ Please enter valid values.")
    else:

        feature_names = [
            'no_of_dependents',
            'education',
            'self_employed',
            'income_annum',
            'loan_amount',
            'loan_term',
            'cibil_score',
            'residential_assets_value',
            'commercial_assets_value',
            'luxury_assets_value',
            'bank_asset_value'
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

        scaled_data = scaler.transform(input_data)

        prediction = model.predict(scaled_data)

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
                margin-top:25px;
            ">
            <h1 style="color:#16a34a;">
            ✅ LOAN APPROVED
            </h1>

            <p style="font-size:18px;color:#2b6a3f;">
            Congratulations! Your loan application has been approved.
            </p>
            </div>
            """, unsafe_allow_html=True)

            st.balloons()

            if os.path.exists(happy_gif):
                st.image(happy_gif, width='stretch')

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
                margin-top:25px;
            ">
            <h1 style="color:#dc2626;">
            ❌ LOAN REJECTED
            </h1>

            <p style="font-size:18px;color:#7a2222;">
            Sorry! Your loan application has been rejected.
            </p>
            </div>
            """, unsafe_allow_html=True)

            if os.path.exists(sad_gif):
                st.image(sad_gif, width='stretch')

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