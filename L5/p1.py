# wapf 1 to find the sum of the digits
#in python first we define the func then we call the function.

def sod(num):
	sum = 0
	while num > 0:
		digit = num % 10      #get last dig
		sum = sum + digit     #use last dig
		num = num // 10       #remove last dig
	else:
		return sum

num = int(input("enter a number "))
if num < 0 :
	print("invalid")
else:
	ans = sod(num)
	print("ans = ", ans)




