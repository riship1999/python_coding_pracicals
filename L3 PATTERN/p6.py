num = int(input("enter lines "))
if num < 0:
	print("invalid")
else:
	c=65
	for i in range(num,0,-1):
		print(i * (chr(c) + "\t"))
		c = c + 1