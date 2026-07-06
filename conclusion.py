import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
dataset = pd.read_csv("flood.csv")
dataset.head()
dataset.shape
dataset.info()
dataset.describe()
dataset.columns
dataset.dtypes
dataset.isnull().sum()
dataset.duplicated().sum()
dataset.drop_duplicates(inplace=True)
dataset.hist(figsize=(15,12))
plt.show()
sns.countplot(x='flood', data=dataset)

plt.title("Flood Distribution")
plt.show()
plt.figure(figsize=(6,5))

sns.boxplot(x='flood', y='ANNUAL', data=dataset)

plt.show()
plt.figure(figsize=(7,5))

sns.scatterplot(x='Humidity', y='ANNUAL', hue='flood', data=dataset)

plt.show()
plt.figure(figsize=(12,10))

sns.heatmap(dataset.corr(),
            annot=True,
            cmap='summer',
            linewidths=1,
            square=True)

plt.title("Correlation Heatmap")

plt.show()
X = dataset.drop("flood", axis=1)

y = dataset["flood"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)
lr = LogisticRegression()

lr.fit(X_train, y_train)

pred_lr = lr.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred_lr))
dt = DecisionTreeClassifier(random_state=42)

dt.fit(X_train, y_train)

pred_dt = dt.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred_dt))
rf = RandomForestClassifier(random_state=42)

rf.fit(X_train, y_train)

pred_rf = rf.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred_rf))
cm = confusion_matrix(y_test, pred_rf)

sns.heatmap(cm,
            annot=True,
            fmt='d',
            cmap='Blues')

plt.xlabel("Predicted")

plt.ylabel("Actual")

plt.show()
print(classification_report(y_test, pred_rf))
accuracy = pd.DataFrame({
    "Model":["Logistic Regression",
             "Decision Tree",
             "Random Forest"],

    "Accuracy":[
        accuracy_score(y_test,pred_lr),
        accuracy_score(y_test,pred_dt),
        accuracy_score(y_test,pred_rf)
    ]
})

accuracy
plt.figure(figsize=(8,5))

plt.bar(accuracy["Model"], accuracy["Accuracy"])

plt.title("Model Accuracy Comparison")

plt.ylabel("Accuracy")

plt.show()
sample = [[29,70,30,3248.6,73.4,386.2,2122.8,666.1,274.8,649.9]]

sample = scaler.transform(sample)

prediction = rf.predict(sample)

if prediction[0]==1:
    print("Flood Expected")
else:
    print("No Flood")
    Import Libraries
        │
        ▼
Load Dataset
        │
        ▼
Descriptive Analysis
        │
        ▼
Data Cleaning
        │
        ▼
Exploratory Data Analysis
   ├── Univariate Analysis
   ├── Bivariate Analysis
   └── Multivariate Analysis
        │
        ▼
Feature Selection
        │
        ▼
Train-Test Split
        │
        ▼
Feature Scaling
        │
        ▼
Train Models
   ├── Logistic Regression
   ├── Decision Tree
   └── Random Forest
        │
        ▼
Evaluate Models
        │
        ▼
Compare Accuracy
        │
        ▼
Predict Flood
        │
        ▼
Conclusion