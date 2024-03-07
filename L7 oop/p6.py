class Person:
	def __init__(self,id,na,ad):
		self.id = id
		self.name = na
		self.address = ad
	def show(self):
		print("id= ",self.id)
		print("name= ",self.name)
		print("address= ",self.address)

class Student(Person):
	def __init__(self,id,na,ad,ma):
		super().__init__(id,na,ad)
		self.marks = ma
	def show(self):
		super().show()
		print("marks = ",self.marks)

class Sport:
	def __init__(self,me):
		self.medals = me
	def show(self):
		print("medals = ",self.medals)

class Result(Student,Sport):
	def __init__(self,id,na,ad,ma,me):
		Student.__init__(self,id,na,ad,ma)  #here we do not write super() call as both student and sport class have init func so as per MRO 
		Sport.__init__(self,me)
	def show(self):
		Student.show(self)
		Sport.show(self)

r = Result(10,"rishi","thane",98,2)
r.show()

	