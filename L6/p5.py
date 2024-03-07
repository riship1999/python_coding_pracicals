#wapp to read sentence and find the word count
# i/p: india america friend india india friend

sentence = input("enter a word")

data = sentence.split(" ")

word_counter = {}
for w in data:
	co = word_counter.get(w)
	if co == None:
		word_counter[w] = 1
	else:	
		word_counter[w] = co + 1

print(word_counter)