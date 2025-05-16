import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

data = pd.read_csv('./heart.csv')

# Heatmap (Correlation)
# plt.figure(figsize=(12, 10))
# sns.heatmap(data.corr(), annot=True, cmap="Blues")
# plt.title("Tương quan đặc trưng")
# plt.tight_layout()
# plt.savefig("heatmap.png", dpi=300)

# Histogram
# features_to_plot = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
# for feature in features_to_plot:
#     plt.figure(figsize=(6, 4))
#     sns.histplot(data[feature], kde=True, color='#4682B4', line_kws={'color': '#F28C38'})
#     plt.title(f'Phân phối {feature}', fontsize=14)
#     plt.xlabel(feature, fontsize=12)
#     plt.ylabel('Số lượng', fontsize=12)
#     plt.tight_layout()
#     plt.savefig(f'histogram_{feature}.png', dpi=300)
#     plt.show()

# Box Plot cho 'age'
plt.figure(figsize=(6, 4))
sns.boxplot(x='target', y='age', data=data, palette=['#1A3C5A', '#F28C38'])
plt.title('Phân phối độ tuổi theo Target', fontsize=14)
plt.xlabel('Target (0: Không bệnh tim, 1: Có bệnh tim)', fontsize=12)
plt.ylabel('Tuổi', fontsize=12)
plt.tight_layout()
plt.savefig('boxplot_age.png', dpi=300)
plt.show()

# Box Plot cho 'chol'
plt.figure(figsize=(6, 4))
sns.boxplot(x='target', y='chol', data=data, palette=['#1A3C5A', '#F28C38'])
plt.title('Phân phối Cholesterol theo Target', fontsize=14)
plt.xlabel('Target', fontsize=12)
plt.ylabel('Cholesterol (mg/dL)', fontsize=12)
plt.tight_layout()
plt.savefig('boxplot_chol.png', dpi=300)
plt.show()

# # Biểu đồ PCA
# from sklearn.decomposition import PCA
# import matplotlib.pyplot as plt
# pca = PCA().fit(X_scaled)
# plt.plot(pca.explained_variance_ratio_, color="#4A90E2")
# plt.title("PCA Explained Variance")
# plt.savefig("pca_plot.png")
#
# # Biểu đồ Loss
# import matplotlib.pyplot as plt
# epochs = range(50)
# loss = [0.5, 0.3, 0.2, 0.1]
# plt.plot(epochs, loss, color="#4A90E2")
# plt.title("Loss qua các vòng lặp")
# plt.savefig("loss_plot.png")
#
# # Biểu đồ Confusion Matrix
# import seaborn as sns
# cm = [[50, 10], [8, 42]]
# sns.heatmap(cm, annot=True, cmap="Blues", fmt="d")
# plt.title("Confusion Matrix")
# plt.savefig("confusion_matrix.png")
#
# # Biểu đồ ROC
# from sklearn.metrics import roc_curve, auc
# fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
# plt.plot(fpr, tpr, color="#4A90E2", label=f"AUC = {auc(fpr, tpr):.2f}")
# plt.plot([0, 1], [0, 1], color="gray", linestyle="--")
# plt.title("ROC Curve")
# plt.savefig("roc_curve.png")
#
# # Biểu đồ Feature Importance
# features = ["thalach", "cp", "age"]
# importance = [0.25, 0.20, 0.15]
# plt.bar(features, importance, color=["#4A90E2", "#F28C38", "#D3D3D3"])
# plt.title("Feature Importance")
# plt.savefig("feature_importance.png")