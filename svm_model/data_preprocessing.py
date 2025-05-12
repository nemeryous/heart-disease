import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_and_preprocess(path='./svm_model/heart_disease_data.csv'):
    df = pd.read_csv(path)
    # Label-encode 'thal'
    df['thal'] = LabelEncoder().fit_transform(df['thal'])
    # Tách X, y
    X = df.drop('target', axis=1)
    y = df['target']
    return X, y