#wapp to write into an existing file.
#filename and data wud be provided by the user

import os.path
filename = input("enter filename to write into ")
if os.path.isfile(filename):
	f =None
	try:
		f = open(filename, "a")
		data  = input("enter data to write ")
		f.write(data + "\n")
	except Exception as e:
		print("write issues ",e)
	finally:
		if f is not None:
			f.close()
else:
	print(filename,"does not exists")



#isfile() returns True only for files
#exists() returns True for files and directory