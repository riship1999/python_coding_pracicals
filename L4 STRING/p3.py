# wapp to read a string and check if its palindrome

s1 = input("enter a string ")

r1 = s1[::-1]
print(r1)

if s1 == r1:
	print("palindrome")
else:
	print("not palindrome")