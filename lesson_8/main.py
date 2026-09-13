import pandas as pd

a=[33,13,24,43,34]
b=pd.Series(a,index=["lelouch","shinji","thorfinn","CHAD","satvik"])
print(b)

data={
    'name':["lelouch","shinji","thorfinn","CHAD","satvik"],
    'country':["britan","japan","norway","mars","pluto"],
    'class':["9A","9B","9C","9D","9E"]
}
b=pd.DataFrame(data)
print(b)
p= pd.read_csv('country_vaccinations.csv')
print(p)
print(p.head())
print(p.tail())