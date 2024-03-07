num = int(input("enter integer "))

if num < 0:
	print("invalid")
else:
	sum,i = 0, 1
	while i <= num:
		sum=sum+i
		i=i+1
	print("sum= ",sum)