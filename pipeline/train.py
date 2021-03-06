from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import joblib


df = pd.read_csv('dataset/data_train.csv')
X = df.drop('y', axis=1)
y = df['y']


model = DecisionTreeClassifier(max_depth=3).fit(X, y)
joblib.dump(model, 'model/m.model')