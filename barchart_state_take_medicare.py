import matplotlib.pyplot as plt
import pandas as pd
 
data = pd.read_csv('state_take_medicare.csv')
df = pd.DataFrame(data)
X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])
plt.bar(X, Y, color='g')
plt.title("Number of unique provider types that take Medicare per state")
plt.xlabel("States")
plt.ylabel("Number of Provider Types")
plt.show()
