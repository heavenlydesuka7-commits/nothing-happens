import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


HouseDF = pd.read_csv(filename)

HouseDF.head()

HouseDF.info()

HouseDF.describe()

HouseDF.columns

sns.pairplot(HouseDF)

plt.figure(figsize=(10, 6))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm',
    linewidths=0.5
)

plt.title("Correlation Heatmap")
plt.show()
