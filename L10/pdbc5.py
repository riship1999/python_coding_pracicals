#wapp to see the record from then user

from sqlite3 import *
con = None
try:
	con = connect("test.db")
	print("connected")
	cur = con.cursor()
	sql = "select * from student"
	cur.execute(sql)
	data = cur.fetchall()              #list of tuple[(rno,name), (rno,name)]
	for d in data:
		print("rno", d[0], "name", d[1])
except Exception as e:
	print("insertion issue ",e)
	con.rollback()                      #dont save record in db
finally:
	if con is not None:
		con.close()
		print("diconnected")