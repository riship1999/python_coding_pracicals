class Book:
	def __init__(self,nop):
		self.nop = nop
	def __add__(self,other):
		res = self.nop + other.nop
		return res
	def __sub__(self,other):
		res = self.nop - other.nop
		return res
	def __mul__(self,other):
		res = self.nop * other.nop
		return res
	
b1 = Book(100)
b2 = Book(200)

r1 = b1 + b2;	print(r1)  #b1 is self and b2 is other, + is calling special method __add__ ,self and other are not keyword they are prefererd words
r2 = b1 - b2;	print(r2)  
r3 = b1 * b2;	print(r3)

