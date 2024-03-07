row = int(input("enter row "))
col = int(input("enter col "))



for i in range(row+1,row+1):
	print(i * ("*"))
	for j in range(col,row+1):
		print(j * ("*"))