class rectangle:
	def __init__(self, le,br):
		self.length = le
		self.breadth = br
	def show(self):
		print("length = ",self.length)
		print("breadth = ",self.breadth)
	def area(self):
		ans = self.length * self.breadth
		print("area = ",ans)
	def perimeter(self):
		ans  = 2 * (self.length + self.breadth)
		print("perimeter = ",ans)

le = float(input("enter length "))
br = float(input("enter breadth "))
r1 = rectangle(le,br)
r1.show()
r1.area()
r1.perimeter()
