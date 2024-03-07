class student:
	def __init__(self, r ,n):
		self.rno = r
		self.name = n
	def talk(self):
		print("my rno is ",self.rno)
		print("my name is ",self.name)

s1 = student(10, "rishi")
s2 = student(20, "patel")
s3 = student(30, "sahil")

s1.talk()
s2.talk()
s3.talk()

# oop: --> it is the way of solving a problem thr class and obj
# class --> encapsulation -->var(rno,name) + method(__int__,talk())
#object --> instantiation --> 3 objects
#reference --> s1,s2,s3
#__init__ --> special function ,self --> used to get the address of the object it is not keyword