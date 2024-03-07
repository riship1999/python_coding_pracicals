'''waoopp for class employee  Instance Var: eid,ename and esalary --> seperate copy
			      Static Var/Class Var: CEO                -->1 copy shared by all obj
			      Parameterized Initializer: for eid,ename and esalary
                              IM: display(),compute_tax() s>5000 --> 20% else 10%
                              SM: display_ceo() '''


class employee: 
	ceo_name = "sundar pichai"
	def __init__(self,id,na,sa):
		self.eid = id
		self.ename = na
		self.esalary = sa
	def display(self):
		print("id= ",self.eid)
		print("name= ",self.ename)
		print("salary= ",self.esalary)
	def compute_taxes(self):
		if self.esalary > 5000:
			amount = self.esalary * 0.20
		else:
			amount = self.esalary * 0.10
		print("tax amount ",amount)	
	@staticmethod
	def display_ceo():
		print("ceo name =",employee.ceo_name)

e1 = employee(10,"rishi",6000)
e1.display()
e1.compute_taxes()
e1.display_ceo()
employee.display_ceo()

e1 = employee(20,"sahil",4000)
e1.display()
e1.compute_taxes()
e1.display_ceo()
employee.display_ceo()

