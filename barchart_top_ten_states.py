import matplotlib.pyplot as plt
import pandas as pd
 
data = pd.read_csv('top_ten_states.csv')
df = pd.DataFrame(data)
X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])
plt.bar(X, Y, color='g')
plt.title("Top ten diverse states by service type")
plt.xlabel("States")
plt.ylabel("Number of Provider Types")
plt.show()
