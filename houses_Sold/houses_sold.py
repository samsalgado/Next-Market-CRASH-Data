from numpy import average
from itertools import groupby
import pandas as pd
load = pd.read_csv("houses_Sold/houses_sold.csv")
load.head()
#housing units in thousands
pre_gold_standard_1963_1972 = [560,565,575,461,487,490,448,485,656]
print(sum(pre_gold_standard_1963_1972)) #4727
print(average(pre_gold_standard_1963_1972)) #525.222
post_gold_standard_1972_1980 = [718, 634,519,549,646,819,817,709,545]
print(sum(post_gold_standard_1972_1980)) #5956
print(average(post_gold_standard_1972_1980)) #661.777
post_gold_standard_decade_1981_1989 = [436,412,623,639,688,750,671,676,650]
print(sum(post_gold_standard_decade_1981_1989)) #5545
print(average(post_gold_standard_decade_1981_1989)) #616.111
post_gold_standard_decade_1990_1999 = [534,509,610,666,670,687,757,804,886,880]
print(sum(post_gold_standard_decade_1990_1999)) #7003
print(average(post_gold_standard_decade_1990_1999)) #700.300
post_gold_standard_decade_2000_2008 = [877, 908,973,1086,1283,1051,776,485]
print(sum(post_gold_standard_decade_2000_2008)) #7439
print(average(post_gold_standard_decade_2000_2008)) #929.825
compare2008_2007 = [{'Year':2007, 'Houses Sold':776}, {'Year':2008, 'Houses Sold':485}]
comparison = groupby(compare2008_2007, key=lambda x:x['Houses Sold'])
for key, value in comparison:
    print(key, list(value))
precollapse_year_2007 = 776
collapse_year_2008 = 485
print(abs(precollapse_year_2007 - collapse_year_2008))
bitcoin_creation_2009_2015 = [375, 323, 306, 368,429,437,501]
print(sum(bitcoin_creation_2009_2015)) #2739
print(average(bitcoin_creation_2009_2015)) #391.28571
rest_until_2016_2021 = [561,613,617,683,822,762]
print(sum(rest_until_2016_2021)) #4058
print(average(rest_until_2016_2021)) #676.333
total_houses_sold_by_era_in_thousands = [{'1963-1972':4727, 'Era':pre_gold_standard_1963_1972}, {'1972-1980':5956, 'Era':post_gold_standard_1972_1980}, {'1981-1989':5545, 'Era':post_gold_standard_decade_1981_1989}, {'1990-1999':7003, 'Era':post_gold_standard_decade_1990_1999}, {'2000-2008':7439, 'Era':post_gold_standard_decade_2000_2008}, {'2009-2015':2739, 'Era':bitcoin_creation_2009_2015}, {'2016-2021':4058, 'Era':rest_until_2016_2021}]
total_by_era = groupby(total_houses_sold_by_era_in_thousands, key=lambda x:x['Era'])
for key, value in total_by_era:
    print(key, list(value))
