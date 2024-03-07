marks=int(input("Enter your marks "))

if marks < 0 or marks > 100:
	print("Marks not in range")
elif marks >= 70:
	print("distinction")
elif marks >= 60:
	print("First Class")
elif marks >= 50:
	print("Second Class")
elif marks >= 40:
	print("Pass Class")
else:
	print("Fail")

