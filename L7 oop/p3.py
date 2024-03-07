class student:
	count = 0
	def __init__(self,r,n,m):
		self.rno = r
		self.name = n
		self.marks = m
	def talk(self):
		print(self.rno, " ", self.name, " ", self.marks)
	@staticmethod
	def show_count():
		print("student count ", student.count)

stu = []
while True:
	op = int(input("1 add,2 view,3 view student count, 4 remove and 5 exit  "))
	if op == 1:
		r = int(input("enter rno "))
		n = input("enter name ")
		m = int(input("enter marks "))
		s = student(r,n,m)
		stu.append(s)
		student.count = student.count + 1
		print("added")
	elif op == 2:
		for s in stu:
			s.talk()
	elif op == 3:
		student.show_count()
	elif op == 4:
		r = int(input("enter rno to remove "))
		for s in stu:
			if s.rno == r:
				stu.remove(s)
				print("removed")
				student.count = student.count - 1
				break
		else: 
			print(r, "does not exists")
	elif op == 5:
		break
	else:
		print("invalid")