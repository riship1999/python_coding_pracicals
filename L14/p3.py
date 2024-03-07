import matplotlib.pyplot as plt

expenses = ['Food','Shopping','Travel','Books']
usages = [500,1000,600,800]
ex_value = [0,0.1,0,0.2]
co_value = ['yellow','blue','brown','red']

plt.pie(usages, labels=expenses, radius=1.2, autopct='%0.2f%%',explode = ex_value,shadow=True,startangle=30,colors= co_value)
plt.axis('equal')
plt.title("Monthly Expenses")
plt.show()

#plt.axis is used to ensure the cicrle looks like circle