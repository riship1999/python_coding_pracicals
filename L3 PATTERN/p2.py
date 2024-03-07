#wapp to generate the following
#	*
#	*	*
#	*	*	*
#	*	*	*	*
# n is given by user

num = int(input("enter number of lines to generate "))
if num < 0:
	print("invalid")
else:
	for i in range(1, num+1):
		print(i * ("*"+"\t")) #\t is tab character