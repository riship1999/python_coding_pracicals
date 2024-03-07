#wapp to insert row into student table

from sqlite3 import *
con = None
try:
	con = connect("employee_database.db")
	print("connected")
	cur = con.cursor()
	sql = "insert into emp values('%d', '%s', '%f') "
	eid = int(input("enter id "))
	ename = input("enter name ")
	esalary = float(input("enter emp salary "))
	cur.execute(sql % (eid , ename , esalary))
	con.commit()    #save the record in db
	print("record saved")
except Exception as e:
	print("insertion issue ",e)
	con.rollback()   #dont save record in db
finally:
	if con is not None:
		con.close()
		print("diconnected")