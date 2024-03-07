#wapp for single inheritance Person and student
class Person:
	def __init__(self,id,na,ad):
		self.id = id
		self.name = na
		self.address = ad
	def show(self):
		print("id=", self.id)
		print("name= ",self.name)
		print("addres= ",self.address)
class Student(Person):
	def __init__(self,id,na,ad,ma):
		super().__init__(id,na,ad)
		self.marks = ma
	def show(self):
		super().show()
		print("marks= ",self.marks)
	
s = Student(10,"rishi","Thane",90)
s.show()