import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="LoanSmart | Dashboard",
    page_icon="📊",
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

.stApp{
    background: linear-gradient(135deg,#f8f5fb,#f2ebf7,#ffffff);
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
    border-right:2px solid rgba(255,255,255,0.08);
}

[data-testid="stSidebar"] *{
    color:white !important;
}

/* TITLE */

.title{
    text-align:center;
    font-size:58px;
    color:#5b1e5c;
    font-weight:800;
    margin-bottom:10px;
    animation:fadeInDown 1s ease;
}

/* SUBTITLE */

.subtitle{
    text-align:center;
    color:#666666;
    font-size:20px;
    margin-bottom:25px;
}

/* BADGES */

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

/* SUB HEADER */

.sub-header{
    font-size:26px;
    color:#5b1e5c;
    font-weight:700;
    margin-bottom:18px;
    margin-top:10px;
}

/* CARD DESIGN */

div[data-testid="stVerticalBlockBorderWrapper"]{
    background:rgba(255,255,255,0.92) !important;
    padding:22px !important;
    border-radius:24px !important;
    box-shadow:0px 8px 24px rgba(0,0,0,0.08) !important;
    border:1px solid rgba(255,255,255,0.3) !important;
    transition:0.3s ease;
    animation:fadeInUp 0.8s ease;
}

/* CARD HOVER */

div[data-testid="stVerticalBlockBorderWrapper"]:hover{
    transform:translateY(-5px);
    box-shadow:0px 12px 28px rgba(91,30,92,0.15) !important;
}

/* METRICS */

div[data-testid="stMetricLabel"] p{
    color:#777777 !important;
    font-size:14px !important;
    font-weight:600 !important;
}

div[data-testid="stMetricValue"] div{
    color:#5b1e5c !important;
    font-size:34px !important;
    font-weight:800 !important;
}

/* DATAFRAME */

[data-testid="stDataFrame"]{
    border-radius:18px;
}

/* CHARTS */

.js-plotly-plot{
    border-radius:18px !important;
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
# LOAD DATASET
# =====================================================

@st.cache_data
def load_data():

    try:

        df = pd.read_csv("dataset/loan_data.csv")

        df.columns = df.columns.str.strip()

        for col in df.columns:

            if df[col].dtype == "object":

                df[col] = df[col].astype(str).str.strip()

        return df

    except:

        data = {
            'loan_id': list(range(1, 101)),
            'no_of_dependents': [2,0,3,1,5]*20,
            'education': ['Graduate','Not Graduate','Graduate','Graduate','Not Graduate']*20,
            'self_employed': ['No','Yes','No','No','Yes']*20,
            'income_annum': [9600000,4100000,9100000,8200000,9800000]*20,
            'loan_amount': [29900000,12200000,29700000,30700000,24200000]*20,
            'loan_term': [12,8,20,8,20]*20,
            'cibil_score': [778,417,506,680,382]*20,
            'residential_assets_value': [2400000,2700000,7100000,18200000,12400000]*20,
            'commercial_assets_value': [17600000,2200000,7000000,3300000,8200000]*20,
            'luxury_assets_value': [22700000,8800000,33300000,23300000,29400000]*20,
            'bank_asset_value': [8000000,3300000,12800000,7900000,5000000]*20,
            'loan_status': ['Approved','Rejected','Rejected','Approved','Rejected']*20
        }

        return pd.DataFrame(data)

df = load_data()

# =====================================================
# PAGE TITLE
# =====================================================

st.markdown("""
<div class='title'>
📊 Dashboard Analytics
</div>

<div class='subtitle'>
AI-Powered Loan Insights & Financial Analytics Dashboard
</div>

<div class='badge-row'>
    <div class='badge'>📈 Smart Analytics</div>
    <div class='badge'>⚡ Real-Time Insights</div>
    <div class='badge'>🏦 Financial Dashboard</div>
    <div class='badge'>📊 Interactive Charts</div>
</div>
""", unsafe_allow_html=True)

# =====================================================
# DATASET PREVIEW
# =====================================================

st.markdown("""
<div class='sub-header'>
📁 Dataset Preview
</div>
""", unsafe_allow_html=True)

with st.container(border=True):

    st.dataframe(
        df.head(10),
        width="stretch"
    )

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# METRICS
# =====================================================

m1, m2, m3, m4 = st.columns(4)

with m1:

    with st.container(border=True):

        st.metric(
            "Total Records",
            f"{len(df):,}"
        )

with m2:

    with st.container(border=True):

        st.metric(
            "Average Income",
            f"₹{int(df['income_annum'].mean()):,}"
        )

with m3:

    with st.container(border=True):

        st.metric(
            "Average Loan",
            f"₹{int(df['loan_amount'].mean()):,}"
        )

with m4:

    with st.container(border=True):

        approval_rate = (
            (df['loan_status'] == "Approved").mean() * 100
        )

        st.metric(
            "Approval Rate",
            f"{approval_rate:.1f}%"
        )

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# PIE CHART
# =====================================================

st.markdown("""
<div class='sub-header'>
📌 Loan Status Distribution
</div>
""", unsafe_allow_html=True)

with st.container(border=True):

    status_counts = (
        df['loan_status']
        .value_counts()
        .reset_index()
    )

    status_counts.columns = ['Status', 'Count']

    fig_pie = px.pie(
        status_counts,
        values='Count',
        names='Status',
        hole=0.45,
        color='Status',
        color_discrete_map={
            'Approved': '#5b1e5c',
            'Rejected': '#d7b7d8'
        }
    )

    fig_pie.update_layout(
        height=500,
        margin=dict(t=20, b=20, l=20, r=20),
        paper_bgcolor='white',
        font_family="Poppins"
    )

    st.plotly_chart(
        fig_pie,
        width="stretch"
    )

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# BAR CHART
# =====================================================

st.markdown("""
<div class='sub-header'>
📈 Average Loan Amount by Education
</div>
""", unsafe_allow_html=True)

with st.container(border=True):

    edu_df = (
        df.groupby('education')['loan_amount']
        .mean()
        .reset_index()
    )

    fig_bar = px.bar(
        edu_df,
        x='loan_amount',
        y='education',
        orientation='h',
        text_auto=True,
        color='education',
        color_discrete_sequence=['#5b1e5c', '#c8a6c9']
    )

    fig_bar.update_layout(
        height=450,
        margin=dict(t=20, b=20, l=20, r=20),
        plot_bgcolor='white',
        paper_bgcolor='white',
        font_family="Poppins",
        xaxis_title="Average Loan Amount",
        yaxis_title="Education"
    )

    st.plotly_chart(
        fig_bar,
        width="stretch"
    )

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# SCATTER PLOT
# =====================================================

st.markdown("""
<div class='sub-header'>
📊 CIBIL Score vs Loan Amount
</div>
""", unsafe_allow_html=True)

with st.container(border=True):

    fig_scatter = px.scatter(
        df,
        x='cibil_score',
        y='loan_amount',
        color='loan_status',
        size='income_annum',
        hover_data=['education', 'self_employed'],
        color_discrete_map={
            'Approved': '#5b1e5c',
            'Rejected': '#d7b7d8'
        }
    )

    fig_scatter.update_layout(
        height=500,
        margin=dict(t=20, b=20, l=20, r=20),
        plot_bgcolor='white',
        paper_bgcolor='white',
        font_family="Poppins"
    )

    st.plotly_chart(
        fig_scatter,
        width="stretch"
    )

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# ASSET BAR CHART
# =====================================================

st.markdown("""
<div class='sub-header'>
🏛️ Average Asset Distribution
</div>
""", unsafe_allow_html=True)

with st.container(border=True):

    asset_data = {

        "Asset Type": [
            "Residential",
            "Commercial",
            "Luxury",
            "Bank"
        ],

        "Average Value": [

            df['residential_assets_value'].mean(),
            df['commercial_assets_value'].mean(),
            df['luxury_assets_value'].mean(),
            df['bank_asset_value'].mean()

        ]
    }

    asset_df = pd.DataFrame(asset_data)

    fig_assets = px.bar(
        asset_df,
        x='Average Value',
        y='Asset Type',
        orientation='h',
        text_auto=True,
        color='Asset Type',
        color_discrete_sequence=[
            '#5b1e5c',
            '#7b4a7c',
            '#9b6b9c',
            '#b38cb4'
        ]
    )

    fig_assets.update_layout(
        height=500,
        margin=dict(t=20, b=20, l=20, r=20),
        plot_bgcolor='white',
        paper_bgcolor='white',
        font_family="Poppins"
    )

    st.plotly_chart(
        fig_assets,
        width="stretch"
    )

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================

st.markdown("""
<div class='footer'>

🏦 LoanSmart Dashboard · Built with Streamlit & Plotly · Developed by Archana

</div>
""", unsafe_allow_html=True)