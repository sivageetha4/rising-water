import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
dataset = pd.read_csv("flood.csv")
dataset.head()
   Temp  Humidity  Cloud Cover  ANNUAL  Jan-Feb  Mar-May  ...
0    29        70           30   3248.6     73.4    386.2 ...
1    28        75           40   3326.6      9.3    275.7 ...
...
dataset.tail()
dataset.shape
(120, 11)
dataset.columns
dataset.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 120 entries
Data columns (total 11 columns):

Temp          int64
Humidity      int64
Cloud Cover   int64
ANNUAL        float64
...
flood         int64
dataset.describe()
| Statistic | Meaning            |
| --------- | ------------------ |
| count     | Number of values   |
| mean      | Average            |
| std       | Standard deviation |
| min       | Minimum value      |
| 25%       | First quartile     |
| 50%       | Median             |
| 75%       | Third quartile     |
| max       | Maximum value      |

dataset.isnull().sum()
dataset.duplicated().sum()
dataset.drop_duplicates(inplace=True)
dataset.dtypes
Temp            int64
Humidity        int64
Cloud Cover     int64
ANNUAL        float64
flood           int64
dataset.nunique()
dataset.corr()
plt.figure(figsize=(12,10))

sns.heatmap(dataset.corr(),
            annot=True,
            cmap='summer',
            linewidths=1)

plt.title("Correlation Heatmap")
plt.show()
sns.countplot(x='flood', data=dataset)

plt.title("Flood Distribution")

plt.show()
