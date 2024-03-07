#wapp to remove a file

import os.path
filename = input("enter file name to delete ")
if os.path.exists(filename):
	os.remove(filename)
	print("file deleted")
else:
	print(filename, "does not exist")