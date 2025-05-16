import os
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from data_preprocessing import load_and_preprocess


def train_svm(test_size=0.3, random_state=42,
              model_dir="./svm_model/models"):
    # 1. Load X, y
    X, y = load_and_preprocess("./svm_model/heart_disease_data.csv")

    # 2. Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state)

    # 3. Tạo pipeline: scale + svm
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('svc',    SVC(kernel='linear', random_state=random_state))
    ])

    # 4. Grid search C
    param_grid = {'svc__C': [0.01, 0.1, 1, 10, 100]}
    grid = GridSearchCV(pipeline, param_grid, cv=5, n_jobs=-1)
    grid.fit(X_train, y_train)

    best_pipeline = grid.best_estimator_
    os.makedirs(model_dir, exist_ok=True)
    joblib.dump(best_pipeline, f"{model_dir}/svm_pipeline.pkl")

    return best_pipeline, X_test, y_test, X.columns.tolist(), grid