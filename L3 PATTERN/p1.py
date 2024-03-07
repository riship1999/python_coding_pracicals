#wapp to read a number and find the factorial

num = int(input("Enter a  number "))
if num < 0:
	print("negative not allowed")
elif num == 0 or num == 1:
	print("fact = ",1)
else:
	f=1
	for i in range(1, num+1):
		f = f * i
	print("fact= ",f)
