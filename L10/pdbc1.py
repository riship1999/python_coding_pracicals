#wapp to connect and disconnect

from sqlite3 import *
con = None
try:
	con = connect("test.db")   #db is not there --> create/open
	print("connected")
except Exception as e:
	print("Connection Issue" ,e)

finally:
	if con is not None:
		con.close()
		print("disconnected")