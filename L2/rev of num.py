#reverse of number
num=int(input("enter a number "))

if num < 0:
	print("invalid")
else:
	print("num= ",num)
	rev = 0
	while num > 0:
		digit = num % 10
		rev = rev * 10 + digit
		num = num // 10
	else:
		print("rev= ",rev)