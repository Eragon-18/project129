import pandas as pd 
import csv 

df1 = pd.read_csv('bright_stars.csv')
df2 = pd.read_csv('dwarf_stars_new.csv')
df = pd.concat([df1, df2])
df.to_csv('merged_stars.csv', index=False)
