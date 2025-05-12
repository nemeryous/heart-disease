import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation(path_csv, output_dir="./svm_model/reports"):
    df = pd.read_csv(path_csv)
    # Nếu cần encode 'thal' giống preprocess
    df['thal'] = pd.Categorical(df['thal']).codes
    corr = df.corr()

    plt.figure(figsize=(12,10))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Correlation Matrix")
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, 'correlation_matrix.png'))
    plt.close()


def plot_distributions(path_csv, output_dir="../reports"):
    df = pd.read_csv(path_csv)
    numeric = ['age','trestbps','chol','thalach','oldpeak']
    plt.figure(figsize=(14,8))
    for i, feat in enumerate(numeric, 1):
        plt.subplot(2,3,i)
        sns.histplot(df[feat], kde=True)
        plt.title(f"Distribution of {feat}")
    plt.tight_layout()
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, 'feature_distributions.png'))
    plt.close()