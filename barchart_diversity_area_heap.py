import matplotlib.pyplot as plt
import pandas as pd
 
data = pd.read_csv('diversity_area_heap.csv')
df = pd.DataFrame(data)

X = list(df.iloc[:, 1])
Y = list(df.iloc[:, 2])

plt.bar(X, Y, color='g')

plt.title("Top 10 diverse service type areas that accepted Medicare in 2019 per area type")
plt.xlabel("Area")
plt.ylabel("Number of Unique Provider Types")

plt.show()