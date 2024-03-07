#wapp to read list of marks from the user and print

marks = []

res = input("do you want to add some marks y/n ")

while res == 'y':
	m = int(input("pls provide marks "))
	marks.append(m)
	res = input("do u want to add some more marks y/n ")

print(marks)

for i in marks:
	print(m)

for m in marks:
	print(m,end = '')