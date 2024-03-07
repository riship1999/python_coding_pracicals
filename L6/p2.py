# wapp to read list of tuple from the user and print the tuple is descending order

list_num, tup_num = [], ()

reply = input("do u want to add some elements y/n ")
while reply == 'y':
	ele = int(input("enter element "))
	list_num.append(ele)
	reply = input("do u want to add some more elements y/n ")

tup_num = tuple(list_num)		# convert list into tuple
print(tup_num)

list_num.sort(reverse=True)

tup_num = tuple(list_num)		# convert list into tuple
print(tup_num)


	

