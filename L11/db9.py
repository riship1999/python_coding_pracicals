#wapp to drop table

from sqlite3 import *
con = None
try:
	con = connect("employee_database.db")
	print("connected")
	cur = con.cursor()
	sql = "drop table emp"
	cur.execute(sql)
	print("table dropped")
	
except exception as e:
	print("drop issue ",e)
	con.rollback()
finally:
	if con is not None:
		con.close()
		print("disconnected")