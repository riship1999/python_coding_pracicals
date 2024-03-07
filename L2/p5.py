#wapp to read attendance value from the user and loop
attdn = int(input("enter attdn "))
if attdn <= 0:
	print("incorrect input")
else:
	i = 1
	while i <= attdn:
		print("i will goto colg",i)
		i = i + 1 
	print("attendance comp")