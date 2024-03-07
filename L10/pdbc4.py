#wapp to insert row into student table

from sqlite3 import *
con = None
try:
	con = connect("test.db")
	print("connected")
	cur = con.cursor()
	sql = "insert into student values('%d', '%s') "
	rno = int(input("enter rno "))
	name = input("enter name")
	cur.execute(sql % (rno,name))
	con.commit()    #save the record in db
	print("record saved")
except Exception as e:
	print("insertion issue ",e)
	con.rollback()   #dont save record in db
finally:
	if con is not None:
		con.close()
		print("diconnected")