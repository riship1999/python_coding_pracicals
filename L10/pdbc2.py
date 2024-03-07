#wapp to create a table

from sqlite3 import *
con = None
try:
	con = connect("test.db")
	print("connected")
	cur = con.cursor()
	sql = "create table student(rno int primary key, name text)"
	cur.execute(sql)
	print("table created")
except Exception as e:
	print("creation issue ",e)
finally:
	if con is not None:
		con.close()
		print("diconnected")