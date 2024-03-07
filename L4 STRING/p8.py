#wapp to read two strings and check if they are anagrams

def mysort(s):
	d = sorted(s)
	ns = ''.join(d)
	return ns

s1 = input("enter first string ")
ns1 = mysort(s1)

s2 = input("enter second string ")
ns2 = mysort(s2)

if ns1 == ns2:
	print("anagram")
else:
	print("not anagrams")
	