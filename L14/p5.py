import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("arrest_data.csv")
print(data)

data['TOTAL_ARRESTS'] = data.sum(axis=1)
print(data)

officer = data['OFFICER_NAME'].tolist()
total = data['TOTAL_ARRESTS'].tolist()
ex_value = [0,0,0.1]

plt.pie(total, labels=officer, autopct='%0.1f%%',explode=ex_value,startangle=90, colors =['g','b','orange'])
plt.axis('equal')
plt.show()