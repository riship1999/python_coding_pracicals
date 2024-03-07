#wapp to implement Data Structure : Stack/LIFO/FIFO

stack = []
while True:
	op = int(input("1 push, 2 pop, 3 display and 4 exit "))
	if op == 1:
		ele = int(input("enter element to push"))
		stack.append(ele)
		print(ele, "is pushed in the stack")
	elif op == 2:
		if len(stack) == 0:
			print("stack is empty")
		else:
			ele = stack.pop()
			print(ele, "is popped")
	elif op == 3:
		print(stack)
	elif op == 4:
		break
	else:
		print("invalid option")