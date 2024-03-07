def f1():
	print("welcome to function")
	print("this is chap 7")

f1()

def f2(a):
	res  = a * a
	print(res)
f2(10)

def f3(a):
	res  = a *  a
	return res
a1 = f3(7)
print(a1)

def f4(a,b):
	res = a + b 
	ares = a - b
	return res,ares
a2, a3 = f4(10,20)
print(a2)
print(a3)