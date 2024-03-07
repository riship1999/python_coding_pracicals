from datetime import * 
d = datetime.now().date()
print(d)

print(d.year)
print(d.day)
print(d.month)


yr = int(input("enter yr in which your are born"))
age = d.year - yr
print('age= ',age)
