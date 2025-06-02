import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OrdinalEncoder, OneHotEncoder

data = pd.read_csv("heart.csv")
# print(data.isnull().sum())
# numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
# plt.figure(figsize=(12, 6))  # Kích thước biểu đồ
# sns.boxplot(data=data[numeric_cols])
# plt.title('Boxplot của các cột số trong dataset')
# plt.xticks(rotation=45)  # Xoay nhãn nếu có nhiều cột
# plt.tight_layout()
# plt.show()

target = "target"
x = data.drop(target, axis=1)
y = data[target]
print(data.head())

# Split data
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=42)

num_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])
ord_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="constant", fill_value="unknown")),
    ("encoder", OrdinalEncoder(categories=[education_values, gender_values, lunch_values, test_values]))
])
nom_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="constant", fill_value="unknown")),
    ("encoder", OneHotEncoder(sparse=False))
])