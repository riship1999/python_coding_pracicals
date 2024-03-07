#wapp to read a string and count the number of letters,digits and other

s1 = input("enter a string ")

lc,dc,oc = 0,0,0

for s in s1:
	if(('A' <= s <= 'Z') or ('a' <= s <= 'z')):
		lc += 1
	elif('0' <= s <= '9'):
		dc += 1
	else:
		oc += 1

print("letters= ",lc, "digits= ",dc, "others= ",oc)
	