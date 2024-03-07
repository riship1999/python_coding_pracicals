#wapp to read two integers and find res = n1 / n2\
#exception - is a runtime error
#exception handlind - to avoid abnormal termination
# try except else finally    raise

print("prcessing started")
try:
	n1 = int(input("enter first number "))
	n2 = int(input("enter secomd number"))
	res = n1 / n2
except ValueError:
	print("u nned to enter integers only")
except ZeroDivisionError:
	print("2nd number should not be 0")
else:
	print("res = ",res)
print("processing ended")