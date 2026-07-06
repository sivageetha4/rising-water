import pandas as pd

df = pd.read_csv("loan_prediction.csv")

print(df.head())
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("loan_prediction.csv")

print(df.head())

print(df.shape)

print(df.columns)

print(df.info())
sns.countplot(x='Loan_Status', data=df)
plt.show()
sns.histplot(df['ApplicantIncome'])
plt.show()
sns.boxplot(x='Loan_Status', y='ApplicantIncome', data=df)
plt.show()
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()
print(df.describe())

print(df.describe(include='object'))
df.fillna(df.mode().iloc[0], inplace=True)
sns.boxplot(df["ApplicantIncome"])
plt.show()
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()

for column in df.columns:
    if df[column].dtype == "object":
        df[column] = encoder.fit_transform(df[column])
        from sklearn.model_selection import train_test_split

X = df.drop("Loan_Status", axis=1)

y = df["Loan_Status"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)
from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier()

dt.fit(X_train, y_train)

print(dt.score(X_test, y_test))
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()

rf.fit(X_train, y_train)

print(rf.score(X_test, y_test))
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()

knn.fit(X_train, y_train)

print(knn.score(X_test, y_test))
from sklearn.ensemble import GradientBoostingClassifier

gb = GradientBoostingClassifier()

gb.fit(X_train, y_train)

print(gb.score(X_test, y_test))
pip install xgboost
from xgboost import XGBClassifier

xgb = XGBClassifier()

xgb.fit(X_train, y_train)

print(xgb.score(X_test, y_test))
print("Decision Tree :", dt.score(X_test, y_test))
print("Random Forest :", rf.score(X_test, y_test))
print("KNN           :", knn.score(X_test, y_test))
print("Gradient Boost:", gb.score(X_test, y_test))
import pickle

pickle.dump(rf, open("rdf.pkl", "wb"))
templates/

home.html

predict.html

submit.html
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("rdf.pkl", "rb"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict")
def predict():
    return render_template("predict.html")

@app.route("/submit", methods=["POST"])
def submit():

    values = [float(x) for x in request.form.values()]

    prediction = model.predict([values])

    if prediction[0] == 1:
        result = "Loan Approved"
    else:
        result = "Loan Rejected"

    return render_template("submit.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
    cd Smart-Lender
    python app.py
    http://127.0.0.1:5000/
    Smart-Lender/
│
├── app.py
├── loan_prediction.csv
├── rdf.pkl
├── requirements.txt
│
├── templates/
│   ├── home.html
│   ├── predict.html
│   └── submit.html
│
├── static/
│   └── style.css
│
└── model_training.py