#wapp to read from an existing file using ARM

import os.path 
filename = input("enter file name to read from ")
if os.path.isfile(filename):
	f = None
	try:
		with open(filename, "r") as f:    #ARM
			data = f.read()
			print(data)
	except Exception as e:
		print("read issue",e)
else:
	print(filename, "does not exist")