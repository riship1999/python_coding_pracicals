#wapp to read list of marks from the user and print
# sum of the marks, average, minimum and maximum

marks = []
res = input("do u want to add some marks y/n ")
while res == 'y':
	m = int(input("pls provide marks "))
	marks.append(m)
	res = input("do you want to add more marks y/n ")

sum = 0
for m in marks:
	sum = sum + m
print("sum = ",sum)

avg = sum/len(marks); print("avg= ",avg )
m1 = min(marks);      print("minimum= ",m1)
m2 = max(marks);      print("maximum", m2)


marks.sort()           #sort in ascending order
m3 = marks[0];          print("minimum = ",m3)
m4 = marks[-1];         print("maximum = ",m4)