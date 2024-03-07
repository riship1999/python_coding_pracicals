#wapp to update record

from sqlite3 import *
con = None
try:
	con = connect("employee_database.db")
	print("connected")
	cur = con.cursor()
	sql = "update emp set ename = '%s' , esalary = '%f' where eid ='%d' "
	eid = int(input("enter emp id to update "))
	ename = input("enter emp name ")
	esalary = float(input("enter emp salary "))
	cur.execute(sql % (ename,esalary,eid))
	con.commit()
	if cur.rowcount > 0:
		print("record added")
	else:
		print("record does not exist")
except exception as e:
	print("update issue ",e)
	con.rollback()
finally:
	if con is not None:
		con.close()
		print("disconnected")