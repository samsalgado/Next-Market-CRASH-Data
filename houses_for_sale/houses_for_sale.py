import pandas as pd
from itertools import groupby 
load = pd.read_csv("houses_Sold/houses_sold.csv")
load.head()
#ALL NUMBERS IN Thousands
pre_gold_Standard = [{'Years':'1963-1972', 'Total':2096}] 
post_gold_Standard_til_2008 = [{'Years':'1973-2008', 'Total':12802}]
post_financial_Collapse_to_2021 = [{'Years':'2009-2021', 'Total':3287}]
Eras = [{'Years':'1963-1972', 'Total':2096},{'Years':'1973-2008', 'Total':12802},{'Years':'2009-2021', 'Total':3287}]
comparison = groupby(Eras, key=lambda x:x['Total'])
for key, value in comparison:
    print(key,list(value))
