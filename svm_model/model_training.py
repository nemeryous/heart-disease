import os
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from data_preprocessing import load_and_preprocess


def train_svm(test_size=0.3, random_state=42, model_dir="./svm_model/models"):
    X, y, scaler, feature_names = load_and_preprocess()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state)

    os.makedirs(model_dir, exist_ok=True)
    joblib.dump(scaler, os.path.join(model_dir, 'scaler.pkl'))

    param_grid = {'C': [0.01,0.1,1,10,100]}
    svc = SVC(kernel='linear', random_state=random_state)
    grid = GridSearchCV(svc, param_grid, cv=5, n_jobs=-1)
    grid.fit(X_train, y_train)

    best_model = grid.best_estimator_
    joblib.dump(best_model, os.path.join(model_dir, 'svm_model.pkl'))

    return best_model, X_test, y_test, feature_names