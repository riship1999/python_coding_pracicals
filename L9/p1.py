#wapp to create class ,its object and save object.

import os.path
import pickle
class student:
	def __init__(self,rno,name):
		self.rno = rno
		self.name = name
	def talk(self):
		print("my rno is ",self.rno)
		print("my name is ",self.name)
stu = []
filename = "student_details.ser"
if os.path.exists(filename):
	f = open(filename, "rb")
	stu = pickle.load(f)
	f.close()
while True:
	op = int(input("1 add,2 view,3 remove,4 exit"))
	if op == 1:
		rno = int(input("enyer rno "))
		name = input("enter name")
		s = student(rno, name)
		stu.append(s)
		print("record added")
	elif op == 2:
		for s in stu:
			s.talk()
	elif op == 3:
		pass
	elif op == 4:
		f = open(filename, "wb")
		pickle.dump(stu,f)
		f.close()
		break
	else:
		print("Invalid option")
	