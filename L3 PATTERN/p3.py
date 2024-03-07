#wapp to generate pattern
#	10
#	20	20
#	30	30	30
#	40	40	40	40

num = int(input("enter number of lines to generate "))
if num < 0:
	print("invalid")
else:
	k=10
	for j in range(1, num+1):          #start-->inclusive,stop-->exclusive
		print(j * (str(k) + "\t")) # *  works with str.
		k = k + 10