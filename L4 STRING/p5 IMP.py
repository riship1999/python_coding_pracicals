'''  
wapp to accept csv and print it
i/p: a,2,b,4,c,3
o/p: 
	a	a
	b	b	b	b
	c	c	c	
imp program as of interview	
'''

s1 = input("enter csv ")
d1 = s1.split(",")
print(d1)

for i in range(0,len(d1),2):
	what = d1[i] + "\t"
	how = int(d1[i+1])  #int() is used to convert string into integer
	print(what * how)
	