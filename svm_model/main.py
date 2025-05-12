from eda import plot_correlation, plot_distributions
from model_training import train_svm
from evaluation import evaluate_and_plot
import os

def main():
    csv_path = "./svm_model/heart_disease_data.csv"

    # 1. EDA
    plot_correlation(csv_path)
    plot_distributions(csv_path)

    # 2. Train
    best_model, X_test, y_test, feature_names = train_svm()

    # 3. Evaluate
    evaluate_and_plot(best_model, X_test, y_test, feature_names)


if __name__ == '__main__':
    main()
