'''
Visualizing the proportion of gender that take Medicare
'''
 
import matplotlib.pyplot as plt
import pandas as pd
 
df = pd.read_csv('corporation_vs_individual.csv')
 
x = list(df.iloc[:, 0])
y = list(df.iloc[:, 1])
 
colors = ["#1f77b4", "#ff7f0e"]
explode = (0, 0)
plt.pie(y, labels=x, explode=explode, colors=colors,
autopct='%1.1f%%', startangle=140)
plt.title("Proportion of individuals vs corporations that took Medicare in 2019")
 
plt.show()
