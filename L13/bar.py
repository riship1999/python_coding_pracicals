import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("student_score.csv")
name = data["NAME"].tolist()
sem1 = data["SEM1"].tolist()

plt.bar(name, sem1, linewidth=5, color='blue')
plt.xlabel("Names")
plt.ylabel("SEM1")
plt.title("Sem1 Performance")
#plt.grid()
plt.show()