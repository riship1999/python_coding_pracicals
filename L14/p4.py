import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("medals.csv")
print(data)
country = data['COUNTRY'].tolist()
g_medal = data['GOLD_MEDAL'].tolist()
ex_value = [0.1,0,0,0]



plt.pie(g_medal,labels=country,autopct='%0.2f%%',explode=ex_value,shadow=True)
plt.axis('equal')
plt.title('Olympics performance')
plt.show()

