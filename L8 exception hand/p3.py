#wapp to read rno and marks from the user

try:
	rno = int(input("enter rno "))
	if rno <= 0:
		raise Exception("rno cannot be -ve")
	marks = int(input("enter marks "))
	if marks < 0 or marks > 100:
		raise Exception("marks out of range")

except ValueError:
	print("u need to enter integers only")
except Exception as e:
	print("issue ",e)
else:
	print("rno = ",rno,"marks= ",marks)