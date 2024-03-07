#wapp to read a string and count no. of letters , digits and others.

s1 = input("enter a string ")

lc, dc, oc = 0,0,0

for s in s1:
	if s.isalpha:
		lc = lc + 1
	elif s.isdigit:
		dc = dc + 1
	else:
		oc = oc + 1

print("letters = ",lc,"digits = ",dc,"others= ",oc)