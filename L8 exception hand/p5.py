#wapp to create a file -> filename would be given by user

import os.path
filename = input("enter file name to create ")
if os.path.exists(filename):
	print(filename,"already exists")
else:
	f = None
	try:
		f = open(filename, "a")
		print(filename, "created")
	except Exception as e:
		print("file creation issue ",e)
	finally:
		if f is not None:
			f.close()