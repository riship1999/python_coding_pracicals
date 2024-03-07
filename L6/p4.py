#wapp to read a word and find letter frequency
#i/p: rishi {i=2,r=1,s=1,h=1}

word  = input("enter a word ")

letter_counter = {}
for w in word:
	co = letter_counter.get(w)
	if co == None:
		letter_counter[w] = 1
	else:
		letter_counter[w] = co + 1

print(letter_counter)