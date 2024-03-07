'''

wapp to read sentence and sort every word in the sentence

'''
def mysort(s):
	d = sorted(s)
	ns = ''.join(d)
	return ns

sentence = input("enter a string ")
data = sentence.split(" ")
new_sentence = ""

for d in data:
	new_sentence = new_sentence + " " + mysort(d)

print(sentence , " " , new_sentence) 
