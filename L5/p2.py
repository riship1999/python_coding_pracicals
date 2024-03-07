#wapp to find sum of digits using recursive


def sod(num):
	if num == 0:
		return 0
	else:
		return (num % 10) + sod(num//10)

num = int(input("enter a number "))
if num < 0:
	print("invalid")
else:
	ans = sod(num)
	print("ans= ",ans)