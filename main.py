import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import pickle


df = pd.read_csv("CarPrice.csv")


print(df.columns)


df = pd.get_dummies(df, drop_first=True)


target_column = "price"


X = df.drop(target_column, axis=1)
y = df[target_column]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


predictions = model.predict(X_test)


score = r2_score(y_test, predictions)

print("\nModel Accuracy:", score)


pickle.dump(model, open("car_price_model.pkl", "wb"))


pickle.dump(X.columns, open("model_columns.pkl", "wb"))

print("\nModel Saved Successfully!")