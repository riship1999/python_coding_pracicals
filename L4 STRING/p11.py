#fact recursive --> func  calling func


def fact(num):
	if num == 1:
		return 1
	else:
		return num * fact(num-1)

num = int(input("enter a number "))

if num < 0:
	print("invalid")
elif num == 0 or num == 1:
	print("fact = ",1)
else:
	ans = fact(num)
	print("fact = ",ans)