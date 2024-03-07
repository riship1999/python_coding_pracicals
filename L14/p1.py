import pandas as pd
import matplotlib.pyplot as plt

months = ['june','july','aug','sep','oct','nov','dec']
mumbai = [82.5,83.06,83.61,85.6,90.75,85.24,84.06]

plt.plot(months, mumbai, linewidth=2, color='blue',marker="o",markersize=10,label='Mumbai')
plt.xlabel("Months")
plt.ylabel("Prices")
plt.title("Petrol Prices")
plt.legend(shadow=True)
plt.grid()
plt.show()