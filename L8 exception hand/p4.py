#wapp to read rno and marks from the user
#used in industries

class InvalidRnoException(Exception):
	def __init__(self,msg):
		self.msg = msg
class InvalidMarksException(Exception):
	def __init__(self,msg):
		self.msg = msg

try:
	rno = int(input("enter rno"))
	if rno <= 0:
		raise InvalidRnoException("rno cannot be -ve")
	marks = int(input("enter marks"))
	if marks < 0 or marks > 100:
		raise InvalidMarksException("marks out of range")
except ValueError:
	print("u need to enter integer only ")
except Exception as e:
	print("issue",e.msg)
else:
	print("rno = ",rno,"marks= ",marks)
		