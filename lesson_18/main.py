import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
uploaded = files.upload()

data = pd.read_csv('Titanic Dataset.csv')

data.head(5)

data.isnull().sum()

age_q1 = np.quantile(data['Age'], 0.25)
age_q2 = np.quantile(data['Age'], 0.50)
age_q3 = np.quantile(data['Age'], 0.75)

print("Age Quartiles ")
print("Q1 - ", age_q1)
print("Q2 - ", age_q2)
print("Q3 - ", age_q3)

IQR_age = age_q3 - age_q1
print("Interquartile Range :", IQR_age)

bins = np.arange(0, 250, 20)
plt.hist(data['Fare'], bins=np.arange(0, 250, 20))

plt.ylabel("count of pasengers")
plt.xlabel("fare")
plt.xticks(bins)