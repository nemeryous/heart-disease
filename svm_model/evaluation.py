import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import (
    classification_report,
    hinge_loss,
    confusion_matrix,
    ConfusionMatrixDisplay,
    roc_curve,
    auc
)


def evaluate_and_plot(
    pipeline, 
    X_test, 
    y_test, 
    feature_names, 
    report_dir="./svm_model/reports"
):
    """
    Đánh giá pipeline (scaler + svc) và vẽ biểu đồ quan trọng.
    pipeline: sklearn Pipeline với bước 'svc'
    X_test, y_test: dữ liệu test
    feature_names: list tên các cột đầu vào
    """
    # 1. Classification report
    y_pred = pipeline.predict(X_test)
    report = classification_report(y_test, y_pred)
    print("Classification Report:\n", report)

    # 2. Feature importances: lấy hệ số từ bước svc trong pipeline
    svc = pipeline.named_steps['svc']
    coefs = abs(svc.coef_[0])
    imp = pd.Series(coefs, index=feature_names).sort_values(ascending=False)

    # 3. Vẽ barplot
    os.makedirs(report_dir, exist_ok=True)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=imp.values, y=imp.index)
    plt.title("Feature Importances (|coef|)")
    plt.tight_layout()
    plt.savefig(os.path.join(report_dir, 'feature_importance.png'))
    plt.close()

def plot_confusion_matrix(pipeline, X_test, y_test, output_dir="./svm_model/reports"):
    y_pred = pipeline.predict(X_test)
    cm = confusion_matrix(y_test, y_pred, labels=[0,1])
    disp = ConfusionMatrixDisplay(cm, display_labels=['No Disease','Disease'])

    os.makedirs(output_dir, exist_ok=True)
    plt.figure()
    disp.plot(cmap='Blues', ax=plt.gca())
    plt.title('Confusion Matrix')
    plt.savefig(f"{output_dir}/confusion_matrix.png")
    plt.close()

def plot_roc_curve(pipeline, X_test, y_test, output_dir="./svm_model/reports"):
    y_scores = pipeline.decision_function(X_test)
    fpr, tpr, _ = roc_curve(y_test, y_scores)
    roc_auc = auc(fpr, tpr)

    os.makedirs(output_dir, exist_ok=True)
    plt.figure()
    plt.plot(fpr, tpr, label=f'ROC Curve (AUC = {roc_auc:.2f})')
    plt.plot([0,1],[0,1],'--',color='grey')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend(loc='lower right')
    plt.savefig(f"{output_dir}/roc_curve.png")
    plt.close()

def plot_decision_score_histogram(pipeline, X_test, y_test, output_dir="./svm_model/reports"):
    y_scores = pipeline.decision_function(X_test)

    os.makedirs(output_dir, exist_ok=True)
    plt.figure()
    plt.hist(y_scores, bins=20)
    plt.title('Histogram of Decision Scores')
    plt.xlabel('Decision Score')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/decision_score_histogram.png")
    plt.close()

def plot_loss_curve_from_cv(grid_search, output_dir="./svm_model/reports"):
    """
    Dùng kết quả GridSearchCV (grid_search.cv_results_) để vẽ loss curve hoặc accuracy curve,
    thay vì fit lại từng model.
    """
    # lấy param C và mean test score
    C = grid_search.param_grid['svc__C']
    mean_scores = grid_search.cv_results_['mean_test_score']
    # hinge loss ngược lại với accuracy
    losses = 1 - mean_scores

    os.makedirs(output_dir, exist_ok=True)
    plt.figure()
    plt.plot(C, losses, marker='o')
    plt.xscale('log')
    plt.xlabel('C')
    plt.ylabel('1 - CV Accuracy')
    plt.title('Approximate Loss Curve vs C')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/loss_curve.png")
    plt.close()