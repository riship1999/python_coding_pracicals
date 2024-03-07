import pandas as pd

data = pd.read_csv("student_score.csv")
print(data)

mumbai_data = data[data.LOCATION == 'MUMBAI']
print(mumbai_data)

thane_data = data[data.LOCATION == 'THANE']
print(thane_data)

data1 = data[data.SEM1 > 70]
print(data1)

data2 = data[ (data.LOCATION == 'MUMBAI') & (data.SEM1 > 70)]
print(data2)

data3 = data[(data.NAME == 'Rumit') | (data.NAME == 'Sumit')]
print(data3)