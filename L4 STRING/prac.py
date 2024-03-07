s1 = input("enter a string ")

vc, cc = 0 ,0
vowel = "a,e,i,o,u,A,E,I,O,U"

for s in s1:
	if s.isalpha():
		if s in vowel:
			vc += 1
		else:
			cc += 1
print("vowels = ",vc,"consonants= ",cc)