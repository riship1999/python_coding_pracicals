#wapp to read 2 strings and check if they are anagrams
#string with same letters but different meaning
#listen silent
#mother inlaw hitler woman


s1 = input("enter string 1 ")
d1 = sorted(s1)
ns1 = ''.join(d1)

s2 = input("enter string 2 ")
d2 = sorted(s2)
ns2 = ''.join(d2)

if ns1 == ns2:
	print("the strings are Anagrams")
else:
	print("not anagrams") 
