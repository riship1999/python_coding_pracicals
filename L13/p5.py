import pandas as pd

data = pd.read_csv("student_score.csv")
print(data)

m1 = data['SEM1'].max()
print(m1)

d1 = data[data.SEM1 == m1]
print(d1)

d2 = data[data.SEM1 == data['SEM1'].max()]
print(d2)

d3 = data[data.SEM1 == data['SEM1'].min()]
print(d3)

d4 = data.sort_values(by='SEM1')
print(d4)

d5 = data.sort_values(by='SEM2',ascending=0)
print(d5)

d6 = data.sort_values(by=['LOCATION', 'NAME'],ascending=[0,1])
print(d6)