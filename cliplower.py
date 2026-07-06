sns.distplot(dataset['Temp'])
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(6,4))
sns.histplot(dataset['Temp'], kde=True, color='skyblue')
plt.title("Distribution of Temperature")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.show()
plt.figure(figsize=(6,4))
sns.kdeplot(dataset['Temp'], fill=True, color='blue')
plt.title("Density Plot of Temperature")
plt.xlabel("Temperature")
plt.show()
num_cols = dataset.select_dtypes(include=['int64', 'float64']).columns

for col in num_cols:
    plt.figure(figsize=(6,4))
    sns.histplot(dataset[col], kde=True)
    plt.title(f"Distribution of {col}")
    plt.show()
    plt.figure(figsize=(6,4))
sns.boxplot(x=dataset['Temp'], color='lightgreen')
plt.title("Box Plot of Temperature")
plt.show()
for col in num_cols:
    plt.figure(figsize=(6,4))
    sns.boxplot(x=dataset[col])
    plt.title(f"Box Plot of {col}")
    plt.show()
    Q1 = dataset['Temp'].quantile(0.25)
Q3 = dataset['Temp'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print("Lower Limit:", lower)
print("Upper Limit:", upper)
outliers = dataset[(dataset['Temp'] < lower) | (dataset['Temp'] > upper)]

print(outliers)
dataset['Temp'] = dataset['Temp'].clip(lower, upper)
sns.boxplot(x=dataset['Temp'])
plt.show()
dataset['Temp'].describe()
print("Skewness:", dataset['Temp'].skew())
import matplotlib.pyplot as plt
import seaborn as sns

# Numerical columns
num_cols = dataset.select_dtypes(include=['int64', 'float64']).columns

for col in num_cols:

    print("\nColumn:", col)
    print(dataset[col].describe())

    plt.figure(figsize=(6,4))
    sns.histplot(dataset[col], kde=True, color='skyblue')
    plt.title(f"Distribution Plot of {col}")
    plt.show()

    plt.figure(figsize=(6,4))
    sns.boxplot(x=dataset[col], color='lightgreen')
    plt.title(f"Box Plot of {col}")
    plt.show()

    print("Skewness:", dataset[col].skew())
    