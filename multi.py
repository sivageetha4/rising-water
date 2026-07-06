import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
df = pd.read_csv("your_dataset.csv")
df.head()
df.info()
df.describe()
df.isnull().sum()
df.fillna(df.mean(), inplace=True)
df.duplicated().sum()
df.drop_duplicates(inplace=True)
df.hist(figsize=(15,10))
plt.show()
sns.countplot(x='target', data=df)
plt.show()
sns.scatterplot(x='age', y='cholesterol', hue='target', data=df)
plt.show()
sns.boxplot(x='target', y='age', data=df)
plt.show()
plt.figure(figsize=(15,15))

sns.heatmap(df.corr(),
            annot=True,
            cmap='summer',
            linewidths=1,
            linecolor='black',
            square=True,
            vmin=-1,
            vmax=1)

plt.title("Correlation Heatmap")
plt.show()
X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = LogisticRegression()

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
cm = confusion_matrix(y_test, y_pred)

sns.heatmap(cm,
            annot=True,
            cmap="Blues",
            fmt='d')

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
print(classification_report(y_test, y_pred))
