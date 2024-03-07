import pandas as pd

data = pd.read_csv("student_score.csv")
print(data)

data1 = data[data.NAME.str.startswith('R')]
print(data1)


data2 = data[data.NAME.str.endswith('na')]
print(data2)

data3 = data[data.NAME.str.contains('um')]
print(data3)




