import seaborn as sns 
import matplotlib.pyplot as plt

df=sns.load_dataset('penguins')
print(df.head())
print(df.tail())
#print(df.info())
#print(df.describe())
print('Species:', df['species'].unique())
print('island:', df['island'].unique())

sns.histplot(data=df, x='body_mass_g', bins=20, color='steelblue')
plt.title('mass of Penguin Body')
plt.xlabel('Body Mass)')
plt.ylabel('Count')
plt.show()

sns.kdeplot(data=df, x='flipper_length_mm', hue='species', fill=True)
plt.title('Flipper Length Shape by Species ')
plt.xlabel('Flipper_Length')
plt.show()


sns.histplot(data=df, x='flipper_length_mm', kde=True, color='magenta')
plt.title('Histogram with KDE Curve')
plt.xlabel('Flipper_Length')
plt.ylabel('Count')
plt.show()

sns.histplot(data=df, x='flipper_length_mm', kde=True, color='blue')
plt.title('Histogram with KDE Curve')
plt.xlabel('Flipper_Length')
plt.ylabel('Count')
plt.show()

corr = df.corr(numeric_only=True)
print(corr)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title(' Heatmap Penguin Measurements')
plt.show()

sns.scatterplot(data=df, x='flipper_length_mm', y='body_mass_g', color='blue')
plt.title('Histogram with KDE Curve')
plt.xlabel('Flipper_Length')
plt.ylabel('Count')
plt.show()