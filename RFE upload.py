# recursive_feature_elimination.py

import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import RFE
from sklearn.model_selection import KFold, cross_val_predict
from sklearn.metrics import r2_score, mean_squared_error

# ============================================================
# 1. Load the dataset after Pearson correlation filtering
#    30 descriptors remain after removing highly correlated
#    features with |r| > 0.8
# ============================================================

data = pd.read_excel(".../pearson_filtered_data.xlsx")

target_col = "Ecorr_统一_true"

feature_cols = [
    col for col in data.columns
    if col != target_col
]

X = data[feature_cols]
y = data[target_col]

print("Number of input features:", X.shape[1])


# ============================================================
# 2. Estimator used for recursive feature elimination
# ============================================================

estimator = RandomForestRegressor(
    n_estimators=...,
    random_state=...
)


# ============================================================
# 3. Cross-validation settings
# ============================================================

cv = KFold(
    n_splits=...,
    shuffle=True,
    random_state=...
)


# ============================================================
# 4. Evaluate different numbers of retained features
# ============================================================

results = []

for n_features in range(1, X.shape[1] + 1):

    selector = RFE(
        estimator=estimator,
        n_features_to_select=n_features,
        step=1
    )

    selector.fit(X, y)

    selected_features = np.array(feature_cols)[selector.support_]

    X_selected = X[selected_features]

    # Cross-validated predictions using the same estimator
    y_pred = cross_val_predict(
        estimator,
        X_selected,
        y,
        cv=cv
    )

    r2 = r2_score(y, y_pred)

    rmse = np.sqrt(
        mean_squared_error(y, y_pred)
    )

    results.append({
        "Number_of_features": n_features,
        "R2": r2,
        "RMSE": rmse,
        "Selected_features": ", ".join(selected_features)
    })

    print(
        f"{n_features:2d} features | "
        f"R2 = {r2:.4f} | "
        f"RMSE = {rmse:.4f}"
    )


# ============================================================
# 5. Save the feature-number comparison
# ============================================================

results_df = pd.DataFrame(results)

results_df.to_excel(
    ".../RFE_results.xlsx",
    index=False
)


# ============================================================
# 6. Determine the optimal number of features
# ============================================================

best_index = results_df["R2"].idxmax()

best_number = results_df.loc[
    best_index,
    "Number_of_features"
]

best_features = results_df.loc[
    best_index,
    "Selected_features"
]

print("\nOptimal number of features:", best_number)
print("Selected features:")
print(best_features)