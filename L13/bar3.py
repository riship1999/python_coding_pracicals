import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("jobs.csv")
language = data["LANGUAGE"].tolist()
jobs_2017 = data["JOBS_2017"].tolist()
jobs_2018 = data["JOBS_2018"].tolist()

x = np.arange(len(language))
plt.bar(x, jobs_2017, label='2017', width=0.25)
plt.bar(x+0.25,jobs_2018,label='2018',width=0.25)
plt.xticks(x,language)      


plt.xlabel("Languages")
plt.ylabel("Jobs")
plt.title("Demand")
plt.grid()
plt.legend(shadow=True)
plt.show()

#xticks is used to print languages name on x axis if we dont write it will print 0,1,2..