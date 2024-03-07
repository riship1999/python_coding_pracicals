class Employee:
	def __init__(self,id,na,pd):
		self.eid = id
		self.ename = na
		self.epds = pd
	def __mul__(self,other):
		res = self.epds * other.nodp
		return res

class Attendance:
	def __init__(self,nodp):
		self.nodp = nodp

e = Employee(10,"amit",1000)
a = Attendance(25)

sal = e * a
print(sal)