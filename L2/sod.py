#sum of digits

num = int(input("Enter a number "))

if num < 0:
	print("invalid")
else:
	sum=0
	while num > 0:
		digit= num % 10     #get last digit
		sum = sum + digit   #use last digit
		num = num // 10     #discard last digit
	else:
		print("sum= ",sum)
		# if while loop gets executed completely