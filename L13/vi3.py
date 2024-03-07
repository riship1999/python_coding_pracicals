import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("petrol_prices.csv")
month = data["MONTH"].tolist()
mumbai = data["MUMBAI"].tolist()
delhi = data["DELHI"].tolist()
chennai = data["CHENNAI"].tolist()

plt.plot(month,mumbai,linewidth=5,linestyle="dashed",marker='p',markersize=10,markerfacecolor='r',label='mumbai')
plt.plot(month,delhi,linewidth=5,linestyle="dotted",marker='o',markersize=10,markerfacecolor='b',label='delhi')
plt.plot(month,chennai,linewidth=5,linestyle="dashdot",marker='d',markersize=10,markerfacecolor='g',label='chennai')



plt.xlabel("Months")
plt.ylabel("Prices")
plt.title("Petrol Prices")
plt.grid()
plt.legend(shadow=True)
plt.show()