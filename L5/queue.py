#wamdpp to implement Data Structure : queue/fifo

queue = []
while True:
	op = int(input("1 insert , 2 remove , 3 display and 4 exit "))
	if op == 1:
		ele = int(input("enter element ti insert "))
		queue.append(ele)
		print(ele, "is inserted in the queue")
	elif op == 2:
		if len(queue) == 0:
			print("queue is empty")
		else:
			ele = queue.pop(0)
			print(ele, "is removed")
	elif op == 3:
		print(queue)
	elif op == 4:
		break
	else:
		print("invalid choice")