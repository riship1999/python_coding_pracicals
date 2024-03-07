# wapp to read list of integers and create even_list and odd_list
# and display even_list in ascending order and odd_list in descending order

org_list, even_list, odd_list = [] , [], []

reply = input("do u want add integers elements y/n ")
while reply == 'y':
	ele = int(input("enter element "))
	org_list.append(ele)
	reply = input("do u want add more integers elements y/n ")

for i in org_list:
	if i%2 == 0:
		even_list.append(i)
	else:
		odd_list.append(i)
even_list.sort()
odd_list.sort(reverse=True)

print("orginal list ", org_list)
print("even list ", even_list)
print("odd list ", odd_list)
	


