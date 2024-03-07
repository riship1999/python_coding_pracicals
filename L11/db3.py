#wapp to insert row into student table

from sqlite3 import *
con = None
try:
	con = connect("employee_database.db")
	print("connected")
	cur = con.cursor()
	sql = "insert into emp values(101, 'raju', 5000) "
	cur.execute(sql)
	con.commit()    #save the record in db
	print("record added in db")
except Exception as e:
	print("insertion issue ",e)
	con.rollback()   #dont save record in db
finally:
	if con is not None:
		con.close()
		print("diconnected")