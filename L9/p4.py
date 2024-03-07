from random import *

while True:
	r1 = randrange(1,10)
	r2 = randrange(1,10)
	r3 = randrange(1,10)
	r4 = randrange(1,10)
	

	r5 = randrange(1,10)
	r6 = randrange(1,10)
	r7 = randrange(1,10)
	r8 = randrange(1,10)


	b1 = (r1+r2+r3+r4) == 21
	b2 = (r5+r6+r7+r8) == 21
	b3 = (r3 == r6)

	if b1 and b2 and b3:
		print("--" * 20)
		print("seq 1-->", r1,r2,r3,r4)
		print("seq 2-->",r5,r6,r7,r8)