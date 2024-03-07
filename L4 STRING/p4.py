#wapp to accept a string which contains csv numbers and add them
# i/p: "10,30,20,50,30"  o/p: 140

s1 = input("enter a csv ")
print(s1)

d1 = s1.split(",")
print(d1)

sum = 0
for d in d1:
	sum = sum + int(d)    #str and int cannot be added hence we use int() to convert str-->int

print(sum)