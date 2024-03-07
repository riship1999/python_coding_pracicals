#wapp to see the record from then user

from sqlite3 import *
con = None
try:
	con = connect("employee_database.db")
	print("connected")
	cur = con.cursor()
	sql = "select * from emp"
	cur.execute(sql)
	data = cur.fetchall()              
	for d in data:
		print("eid = ", d[0], "ename = ", d[1], " esalary = ",d[2])
except Exception as e:
	print("insertion issue ",e)
	con.rollback()                      #dont save record in db
finally:
	if con is not None:
		con.close()
		print("diconnected")