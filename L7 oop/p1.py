'''waoopp for class circle  IV:	radius
			    IM: show(),area(),circumference()
                            PI: for initializing radius'''

class circle:
	def __init__(self, r):
		self.radius = r
	def show(self):
		print("radius= ",self.radius)
	def area(self):
		ans = 3.14159 * self.radius ** 2
		print("area = ",round(ans,2))
	def circumference(self):
		ans = 2 * 3.14159 * self.radius
		print("circumference =",round(ans,3))

rad = float(input("enter radius "))
c1 = circle(rad)
c1.show()
c1.area()
c1.circumference()