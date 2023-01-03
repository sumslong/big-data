'''
Visualizing the proportion of gender that take Medicare
'''
 
import matplotlib.pyplot as plt
import pandas as pd
 
df = pd.read_csv('gender_take_medicare.csv')
 
x = list(df.iloc[:, 0])
y = list(df.iloc[:, 1])
 
colors = ["#1f77b4", "#ff7f0e"]
explode = tuple([0]*len(x))
plt.pie(y, labels=x, explode=explode, colors=colors,
autopct='%1.1f%%', shadow=False, startangle=140)
plt.title("Proportion of genders of providers who took Medicare in 2019")
 
plt.show()
