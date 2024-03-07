#wapp to read string from user and print the string
#1> all character on same line
#2> each on different on separate line

s1 = input("enter a string ")

print(s1)

for i in range(len(s1)):
	print(s1[i])

for j in s1:
	print(j)