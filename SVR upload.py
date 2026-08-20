# svr_model.py

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.metrics import r2_score, mean_squared_error

# ============================================================
# 1. Load data
# ============================================================
data = pd.read_excel(".../original_data.xlsx")

feature_cols = [
    "electrical_resistivity_std",
    "thermal_conductivity_std/mean*100",
    "thermal_conductivity_mean",
    "liquid_range_std",
    "X_mean",
    "Ni",
    "Cu"
]

target_col = "Ecorr_统一_true"

X = data[feature_cols]
y = data[target_col]

# ============================================================
# 2. Train-test split
# Use the same split for all regression models
# ============================================================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=...,
    random_state=...
)

# ============================================================
# 3. Feature standardization
# ============================================================
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ============================================================
# 4. SVR model
# Hyperparameters should be set according to the study settings
# ============================================================
model = SVR(
    kernel="rbf",
    C=...,
    gamma=...,
    epsilon=...
)

model.fit(X_train_scaled, y_train)

# ============================================================
# 5. Prediction and evaluation
# ============================================================
y_train_pred = model.predict(X_train_scaled)
y_test_pred = model.predict(X_test_scaled)

train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

train_rmse = np.sqrt(mean_squared_error(y_train, y_train_pred))
test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))

print("SVR")
print("Training R2:", train_r2)
print("Testing R2:", test_r2)
print("Training RMSE:", train_rmse)
print("Testing RMSE:", test_rmse)

# Optional output
results = pd.DataFrame({
    "Experimental": y_test.values,
    "Predicted": y_test_pred
})

results.to_excel(".../SVR_prediction_results.xlsx", index=False)