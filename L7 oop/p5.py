#wapp for multilevel inheritence

class Person:
	def __init__(self,id,na,ad):
		self.id = id
		self.name = na
		self.address = ad
	def show(self):
		print("id= ",self.id)
		print("name= ",self.name)
		print("address= ",self.address)
class Teacher(Person):
	def __init__(self,id,na,ad,sa):
		super().__init__(id,na,ad)
		self.salary = sa
	def show(self):
		super().show()
		print("salary = ",self.salary)
class Hod(Teacher):
	def __init__(self,id,na,ad,sa,de):
		super().__init__(id,na,ad,sa)
		self.dept = de
	def show(self):
		super().show()
		print("dept = ",self.dept)

h = Hod(10,"ashish","Kharghar",1000,'comps')
h.show()