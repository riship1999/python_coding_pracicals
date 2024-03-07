#leap yr
#come after 4 yrs if the yr is non century
#comes after 400 yrs if the yr is century(ending 00 )

year=int(input("enter a yr "))

b1 = (year%100 == 0) and (year%400 == 0)
b2 = (year%100 != 0) and (year%4 == 0)

if b1 or b2:
	print("it is leap yr")
else:
	print("it is not leap yr")