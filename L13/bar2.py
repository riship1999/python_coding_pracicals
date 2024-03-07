import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("student_score.csv")
name = data["NAME"].tolist()
sem1 = data["SEM1"].tolist()
sem2 = data["SEM2"].tolist()

x = np.arange(len(name))
plt.bar(x, sem1, label='sem1', width=0.25)
plt.bar(x+0.25,sem2,label='sem2',width=0.25)
plt.xticks(x,name)

plt.xlabel("Names")
plt.ylabel("sem")
plt.title("Sem1 and Sem2 performace")
plt.grid()
plt.legend(shadow=True)
plt.show()

