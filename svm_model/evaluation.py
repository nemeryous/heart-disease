import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report


def evaluate_and_plot(model, X_test, y_test, feature_names, report_dir="./svm_model/reports"):
    # 1. Classification report
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)
    print("Classification Report:\n", report)

    # 2. Feature importances for linear SVM
    coefs = abs(model.coef_[0])
    imp = pd.Series(coefs, index=feature_names).sort_values(ascending=False)

    plt.figure(figsize=(10,6))
    sns.barplot(x=imp.values, y=imp.index)
    plt.title("Feature Importances (|coef|)")
    os.makedirs(report_dir, exist_ok=True)
    plt.savefig(os.path.join(report_dir, 'feature_importance.png'))
    plt.close()