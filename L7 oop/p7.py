class Employee:
	def __init__(self,id,na,sa):
		self.id = id
		self.name = na
		self.salary = sa
	def bonus(self):
		amt = self.salary * 0.10
		print("bonus amt = ",amt)

class AEmployee(Employee):
	pass

class PEmployee(Employee):
	def bonus(self):
		amt = self.salary * 0.15
		print("bonus amt= ",amt)

class Manager(Employee):
	def bonus(self):
		amt = self.salary * 0.20
		print("bonus amt= ",amt)

a = AEmployee(10,"amit",1000);	      a.bonus()
p = PEmployee(20, "sumit",2000);      p.bonus()
m = Manager(30, "rumit",5000);        m.bonus()