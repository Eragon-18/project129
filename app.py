import pandas as pd 
import csv

df = pd.read_csv('dwarf_stars.csv')
df = df.dropna()

m = []
for i in df['Mass']:
    i = float(i) * 0.000954588
    m.append(i)

r = []
for j in df['Radius']:
    j = float(j) * 0.102763
    r.append(j)

df['Mass'] = m 
df['Radius'] = r

df.to_csv('dwarf_stars_new.csv', index=False)