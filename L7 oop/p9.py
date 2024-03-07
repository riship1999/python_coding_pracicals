# operator overloading,method over-riding
class Mech:
	def __init__(self,price):
		self.price = price
	def __add__(self,other):
		ans = self.price + other.amount
		return ans
	def __sub__(self,other):
		ans = self.price - other.amount
		return ans
class Bee:
	def __init__(self,amount):
		self.amount = amount
	def __sub__(self,other):
		ans = self.amount - other.price
		return ans

m = Mech(750) 
b = Bee(350)  


r1 = m + b;  print(r1)
r2 = m - b;  print(r2)
r3 = b - m;  print(r3)