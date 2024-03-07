#	*	*	*	*
#	*	*	*
#	*	*
#	*

num = int(input("Enter number of lines to generate "))
if num < 0:
	print("invalid")
else:
	for i in range(num, 0 , -1):
		print(i * ("*" + "\t"))