#wapp to create a table

from sqlite3 import *
con = None
try:
	con = connect("employee_database.db")
	print("connected")
	cur = con.cursor()
	sql = "create table emp(eid int primary key, ename text, esalary double)"
	cur.execute(sql)
	print("table created")
except Exception as e:
	print("creation issue ",e)
finally:
	if con is not None:
		con.close()
		print("diconnected")