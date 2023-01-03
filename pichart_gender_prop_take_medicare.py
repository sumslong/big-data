'''
Visualizing the proportion of gender / total that take Medicare
'''
 
import matplotlib.pyplot as plt
import pandas as pd
 

data = pd.read_csv('gender_prop_take_medicare.csv')
df = pd.DataFrame(data)
X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])
plt.bar(X, Y, color='g')
plt.title("Percentage of each gender who took Medicare versus total in US")
plt.xlabel("Gender")
plt.ylabel("Percentage of Providers")
plt.show()

# df = pd.read_csv('gender_prop_take_medicare.csv')
 
# x = list(df.iloc[:, 0])
# y = list(df.iloc[:, 1])
 
# colors = ["#1f77b4", "#ff7f0e"]
# explode = tuple([0]*len(x))
# plt.pie(y, labels=x, explode=explode, colors=colors,
# autopct='%1.1f%%', shadow=False, startangle=140)
# plt.title("Proportion of genders of providers who took Medicare in 2019")
 
# plt.show()


