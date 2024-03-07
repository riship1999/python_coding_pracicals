#wapp to insert row into student table

from sqlite3 import *
con = None
try:
	con = connect("test.db")
	print("connected")
	cur = con.cursor()
	sql = "insert into student values(10, 'amit') "
	cur.execute(sql)
	con.commit()    #save the record in db
	print("record saved")
except Exception as e:
	print("insertion issue ",e)
	con.rollback()   #dont save record in db
finally:
	if con is not None:
		con.close()
		print("diconnected")