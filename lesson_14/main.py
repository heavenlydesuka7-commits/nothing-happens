import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

filename = "USA_Housing.csv"


HouseDF = pd.read_csv(filename)



print(HouseDF.head())


HouseDF.info() 

print(HouseDF.describe())

print(HouseDF.columns)


sns.pairplot(HouseDF)
plt.show()  

numeric_df = HouseDF.select_dtypes(include=[np.number])


plt.figure(figsize=(10, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.tight_layout()  
plt.show()

