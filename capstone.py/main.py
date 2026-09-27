import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#1
df=sns.load_dataset('penguins')
#2
print(df.head(10))
#3
print(df.tail(5))
#4
print(df.dtypes)
print(df.info())
print(df.describe())
#5
print(df['species'].unique())
print(df['species'].value_counts())
print(df['island'].unique())
print(df['island'].value_counts())
print(df['sex'].unique())
print(df['sex'].value_counts())
#6
a=df.corr(numeric_only=True)
print(a)
#7
sns.heatmap(data=a,annot=True)
plt.show()

#8
b=df.select_dtypes(include='number')
b.hist(figsize=(10,8))
plt.show()

#9
b.plot(kind='box',subplots=True,figsize=(10,8))
plt.show()

#10
sns.countplot(x='species',data=df)
plt.show()

#11
sns.countplot(x='island',data=df)
plt.show()

#12
sns.countplot(x='sex',data=df)
plt.show()

#13
sns.scatterplot(x='flipper_length_mm',y='body_mass_g',hue='species',data=df)
plt.show()

#14
sns.scatterplot(x='bill_length_mm',y='bill_depth_mm',hue='species',data=df)
plt.show()

#15
sns.boxplot(x='species',y='body_mass_g',data=df)
plt.show()

#16
sns.pairplot(df[['bill_depth_mm','flipper_length_mm','body_mass_g']])
plt.show()
