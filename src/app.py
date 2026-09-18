import streamlit as st
import pandas as pd
import joblib
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="FraudGuard AI",
    page_icon="💳",
    layout="wide"
)

# ---------------- STYLE ----------------
st.markdown("""
<style>
.main {
    background-color: #0f172a;
}

.block-container {
    padding-top: 2rem;
}

.hero {
    padding: 30px;
    border-radius: 20px;
    background: linear-gradient(135deg, #1e293b, #172554);
    border: 1px solid #334155;
    margin-bottom: 25px;
}

.hero h1 {
    color: white;
    font-size: 42px;
    margin-bottom: 5px;
}

.hero p {
    color: #cbd5e1;
    font-size: 18px;
}

.card {
    padding: 20px;
    border-radius: 16px;
    background: #1e293b;
    border: 1px solid #334155;
    margin-bottom: 20px;
}

.success-box {
    padding: 25px;
    border-radius: 16px;
    background: #064e3b;
    border: 1px solid #10b981;
    text-align: center;
    color: white;
    font-size: 22px;
}

.danger-box {
    padding: 25px;
    border-radius: 16px;
    background: #450a0a;
    border: 1px solid #ef4444;
    text-align: center;
    color: white;
    font-size: 22px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("💳 FraudGuard AI")
st.sidebar.write("Credit Card Fraud Detection")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "🔍 Fraud Detection",
        "📊 Dataset Analysis"
    ]
)

# ---------------- LOAD DATA ----------------
DATA_PATH = "data/creditcard.csv"
MODEL_PATH = "src/models/fraud_model.pkl"

if not os.path.exists(DATA_PATH):
    st.error("Dataset not found.")
    st.stop()

data = pd.read_csv(DATA_PATH)

if not os.path.exists(MODEL_PATH):
    st.error("Model not found. Run train_model.py first.")
    st.stop()

model = joblib.load(MODEL_PATH)

# =========================================================
# DASHBOARD
# =========================================================

if page == "🏠 Dashboard":

    st.markdown("""
    <div class="hero">
        <h1>💳 FraudGuard AI</h1>
        <p>Intelligent Credit Card Fraud Detection System</p>
    </div>
    """, unsafe_allow_html=True)

    total = len(data)
    normal = int((data["Class"] == 0).sum())
    fraud = int((data["Class"] == 1).sum())

    st.subheader("📊 System Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("💳 Total Transactions", f"{total:,}")

    with col2:
        st.metric("✅ Normal Transactions", f"{normal:,}")

    with col3:
        st.metric("🚨 Fraudulent Transactions", f"{fraud:,}")

    st.subheader("📈 Transaction Distribution")

    chart_data = pd.DataFrame({
        "Transaction Type": ["Normal", "Fraud"],
        "Count": [normal, fraud]
    })

    st.bar_chart(
        chart_data.set_index("Transaction Type")
    )

# =========================================================
# FRAUD DETECTION
# =========================================================

elif page == "🔍 Fraud Detection":

    st.markdown("""
    <div class="hero">
        <h1>🔍 Fraud Detection</h1>
        <p>Upload transaction data and analyze it using the trained machine learning model.</p>
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Upload Transaction CSV",
        type=["csv"]
    )

    if uploaded_file:

        uploaded_data = pd.read_csv(uploaded_file)

        st.subheader("📄 Uploaded Data")
        st.dataframe(
            uploaded_data,
            use_container_width=True
        )

        prediction_data = uploaded_data.copy()

        if "Class" in prediction_data.columns:
            prediction_data = prediction_data.drop(
                columns=["Class"]
            )

        try:

            predictions = model.predict(prediction_data)

            uploaded_data["Prediction"] = predictions

            fraud_count = int((predictions == 1).sum())
            normal_count = int((predictions == 0).sum())

            st.subheader("📊 Prediction Results")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "✅ Normal",
                    normal_count
                )

            with col2:
                st.metric(
                    "🚨 Fraud",
                    fraud_count
                )

            if fraud_count > 0:

                st.markdown(
                    f"""
                    <div class="danger-box">
                        🚨 {fraud_count} Potential Fraudulent Transaction(s) Detected
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    """
                    <div class="success-box">
                        ✅ No Fraudulent Transactions Detected
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.subheader("📋 Detailed Predictions")

            st.dataframe(
                uploaded_data,
                use_container_width=True
            )

        except Exception as e:

            st.error(
                f"Prediction error: {e}"
            )

# =========================================================
# DATASET ANALYSIS
# =========================================================

elif page == "📊 Dataset Analysis":

    st.markdown("""
    <div class="hero">
        <h1>📊 Dataset Analysis</h1>
        <p>Explore the credit card transaction dataset.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Dataset Size")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Rows",
            f"{data.shape[0]:,}"
        )

    with col2:
        st.metric(
            "Columns",
            data.shape[1]
        )

    st.subheader("🚨 Fraud vs Normal")

    counts = data["Class"].value_counts()

    chart = pd.DataFrame({
        "Type": ["Normal", "Fraud"],
        "Transactions": [
            int(counts.get(0, 0)),
            int(counts.get(1, 0))
        ]
    })

    st.bar_chart(
        chart.set_index("Type")
    )

    st.subheader("💰 Transaction Amount")

    st.line_chart(
        data["Amount"].head(500)
    )

    st.subheader("📋 Dataset Preview")

    st.dataframe(
        data.head(100),
        use_container_width=True
    )

# ---------------- FOOTER ----------------

st.markdown("""
<hr>
<div style="text-align:center;color:#94a3b8;">
    FraudGuard AI • Credit Card Fraud Detection • Machine Learning
</div>
""", unsafe_allow_html=True)