#pattern a-97,b-98...  A-65,B-66..
#	a
#	b	b
#	c	c	c
#	d	d	d	d

num = int(input("enter number "))
if num < 0:
	print("invalid")
else:
	c=97
	for k in range(1, num+1):
		print(k * (chr(c) + "\t"))
		c = c + 1