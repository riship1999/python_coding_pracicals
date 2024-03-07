# wamdpp to maintain the name of ipl teams

ipl_team_names = set()

while True:
	op = int(input("1 add, 2 view, 3 remove and 4 exit "))
	if op == 1:
		initial_size = len(ipl_team_names)
		name = input("enter team name ")
		ipl_team_names.add(name)
		final_size = len(ipl_team_names)
		if final_size > initial_size:
			print(name, " has been added ")
		else:
			print(name , " already exists ")
	elif op == 2:
		print(ipl_team_names)
	elif op == 3:
		initial_size = len(ipl_team_names)
		name = input("enter team name to remove ")
		ipl_team_names.discard(name)    #remove() gives exception
		final_size = len(ipl_team_names)
		if final_size < initial_size:
			print(name, "has been removed")
		else:
			print(name, "does not exist")
	elif op == 4:
		break
	else:
		print("invalid option ")
		