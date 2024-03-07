import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("student_score.csv")
name = data["NAME"].tolist()
sem1 = data["SEM1"].tolist()
sem2 = data["SEM2"].tolist()

plt.plot(name,sem1,linewidth=5,marker='p',markersize=10,markerfacecolor='r',label='sem1')
plt.plot(name,sem2,linewidth=5,marker='o',markersize=10,markerfacecolor='b',label='sem2')


plt.xlabel("Names")
plt.ylabel("sem")
plt.title("Sem1 and Sem2 performace")
plt.grid()
plt.legend(shadow=True)
plt.show()


#legend will be displayed only when label is given