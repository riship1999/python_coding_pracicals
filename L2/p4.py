n1=int(input("enter first number "))
n2=int(input("enter second number "))
n3=int(input("enter third number "))

if n1 > n2:
	m1 = n1
else:
	m1 = n2
if n3 > m1:
	m1 = n3

print("max of 3 = ",m1)

res = max(n1,n2,n3)
print("res = ", res)


res1 = min(n1,n2,n3)
print("res = ", res1)

