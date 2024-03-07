#wapp to delete record

from sqlite3 import *
con = None
try:
	con = connect("employee_database.db")
	print("connected")
	cur = con.cursor()
	sql = "delete from emp where eid = '%d' "
	eid = int(input("enter emp id to delete "))
	cur.execute(sql % (eid))
	con.commit()
	if cur.rowcount > 0:
		print("record deleted")
	else:
		print("record does not exist")
except exception as e:
	print("delete issue ",e)
	con.rollback()
finally:
	if con is not None:
		con.close()
		print("disconnected")