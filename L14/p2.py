import matplotlib.pyplot as plt
import numpy as np


products = ['Laptop','Printer','Router']
Reena = [10,25,15]
Veena = [5,30,12]

x = np.arange(len(products))
plt.bar(x, Reena, label='Reena', width=0.25)
plt.bar(x+0.25,Veena,label='Veena',width=0.25)
plt.xticks(x,products)

plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Performance Analysis")
plt.grid()
plt.legend(shadow=True)
plt.show()

