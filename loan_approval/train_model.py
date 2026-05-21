import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
import joblib

# =====================================================
# LOAD DATASET
# =====================================================

df = pd.read_csv("dataset/loan_data.csv")

# REMOVE EXTRA SPACES FROM COLUMN NAMES
df.columns = df.columns.str.strip()

# REMOVE EXTRA SPACES FROM VALUES
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].astype(str).str.strip()

print("✅ Dataset Loaded Successfully")

# =====================================================
# ENCODING
# =====================================================

df['education'] = df['education'].map({
    'Graduate': 1,
    'Not Graduate': 0
})

df['self_employed'] = df['self_employed'].map({
    'Yes': 1,
    'No': 0
})

df['loan_status'] = df['loan_status'].map({
    'Approved': 1,
    'Rejected': 0
})

# =====================================================
# REMOVE NULL VALUES
# =====================================================

df.dropna(inplace=True)

# =====================================================
# FEATURES & TARGET
# =====================================================

X = df.drop(['loan_id', 'loan_status'], axis=1)

y = df['loan_status']

print("\n📌 Features Used:")
print(X.columns)

# =====================================================
# TRAIN TEST SPLIT
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =====================================================
# FEATURE SCALING
# =====================================================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

# =====================================================
# MODEL TRAINING
# =====================================================

model = LogisticRegression(max_iter=2000)

model.fit(X_train, y_train)

print("\n✅ Model Training Completed")

# =====================================================
# EVALUATION
# =====================================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\n🎯 Accuracy Score:", accuracy)

print("\n📊 Classification Report:\n")

print(classification_report(y_test, y_pred))

# =====================================================
# SAVE MODEL & SCALER
# =====================================================

joblib.dump(model, "model.pkl")

joblib.dump(scaler, "scaler.pkl")

print("\n✅ model.pkl Saved")

print("✅ scaler.pkl Saved")