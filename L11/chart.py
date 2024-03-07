from sqlite3 import *
import matplotlib.pyplot as plt
import numpy as np

con = None
try:
	con = connect("student_database.db")
	print("connected")
	cur = con.cursor()
	sql = "select * from st"
	cur.execute(sql)
	data = cur.fetchall()              #list of tuple[(rno,name,mark), (rno,name,mark)]

	roll = []
	name = []
	mark = []	
	
	for d in data:
		roll.append(d[0])
		name.append(d[1])
		mark.append(d[2])
	x = np.arange(len(name))

	plt.bar(x, mark, label='mark', width=0.25)
	plt.bar(x+0.25,roll,label='roll',width=0.25)
	plt.xticks(x,name)
	
	for marks,roll in enumerate(roll):
		plt.text(marks + 0.27  , roll  , str(roll), color='orange',fontweight='bold',ha='center',va='bottom')
	
	
	plt.grid()
	plt.legend(shadow=True)
	plt.show()	
	
except Exception as e:
	print("insertion issue ",e)
	con.rollback()                      #dont save record in db
finally:
	if con is not None:
		con.close()
		print("diconnected")