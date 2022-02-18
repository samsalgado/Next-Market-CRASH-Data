import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt 
load = pd.read_csv("CSVs/usprice_cust.csv")
load.head()
data = {1972:27600, 1984:79900, 1992:121500, 2002:187600, 2008:232100, 2021:392900}
Years = list(data.keys())
Median_Prices = list(data.values())
plt.bar(Years,Median_Prices)
median_house_1972 = 121500
median_house_2021 = 392900
inflation_rate_2021_1972 =  lambda x,y : x/y
print(inflation_rate_2021_1972(median_house_1972, median_house_2021))
inflation_rate = "30%"
