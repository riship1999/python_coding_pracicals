from datetime import *

d = datetime.now()
print(d)

h = d.hour
print(h)
print(d.minute)
print(d.second)
print(d.microsecond)

if h>=6 and h<12:
	print("gm")
elif h>=12 and h<17:
	print("ga")
else:
	print("ge")