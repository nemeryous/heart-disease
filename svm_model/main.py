from eda import plot_correlation, plot_distributions
from model_training import train_svm
from evaluation import evaluate_and_plot
from evaluation import (
    plot_confusion_matrix,
    plot_roc_curve,
    plot_decision_score_histogram,
    plot_loss_curve_from_cv
)
import os

def main():
    csv_path = "./svm_model/heart_disease_data.csv"

    # 1. EDA
    plot_correlation(csv_path)
    plot_distributions(csv_path)

    # 2. Train
    best_pipeline, X_test, y_test, feat_names, grid = train_svm()

    # 3. Evaluate
    evaluate_and_plot(best_pipeline, X_test, y_test, feat_names)
    plot_confusion_matrix(best_pipeline, X_test, y_test)
    plot_roc_curve(best_pipeline, X_test, y_test)
    plot_decision_score_histogram(best_pipeline, X_test, y_test)
    plot_loss_curve_from_cv(grid)

if __name__ == '__main__':
    main()
