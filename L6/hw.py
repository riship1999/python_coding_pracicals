#wamdpp to maintain station names with corona count

corona_counter = {}

while True:
	op = int(input("1 add, 2 view, 3 update, 4 remove,5 exit "))
	if op == 1:
		sn = input("enter station name ")
		ch = corona_counter.get(sn)
		if ch == None:
			co = int(input("enter count "))
			corona_counter[sn] = co
			print(sn, "has been added")
			print(corona_counter)
		else:
			print(sn, "already exists")
	elif op == 2:
		print(corona_counter)
	elif op == 3:
		stn = input("enter station to update ")
		ch = corona_counter.get(stn)
		if ch == None:
			print("Station not added")
		else:
			co = int(input("enter the updated count "))
			corona_counter.update({stn:co})
			print(stn, "has been updated")
			print(corona_counter)
	elif op == 4:
		sn = input("enter station name to remove ")
		ch = corona_counter.get(sn)
		if ch == None:
			print("Station does not exist")
		else:
			del_ele = corona_counter.pop(sn)
			print(sn, "has been removed")
			print(corona_counter)
	elif op == 5:
		break
	else:
		print("invalid")


