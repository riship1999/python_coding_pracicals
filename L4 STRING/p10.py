#wapp to find fact of num

def fact(num):
	f = 1
	for i in range(1,num+1):
		f = f * i
	else:
		return f

num = int(input("enter a number "))

if num < 0:
	print("invalid")
elif num == 0 or num == 1:
	print("fact = ",1)
else:
	ans = fact(num)
	print("fact = ",ans)