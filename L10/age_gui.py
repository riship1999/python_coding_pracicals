from tkinter import *
from tkinter.messagebox import *
from datetime import *

root = Tk()
root.title("Age Calci")
root.geometry("600x400+500+200")

lb1Number = Label(root, text="enter dob --> dd/mm/yyyy", font=('courier',24, 'bold italic'))
lb1Number.pack(pady=10)

entNumber = Entry(root, bd=5, font=('courier',24,'bold italic'))
entNumber.pack(pady=10)
entNumber.focus()

def age():
	try:
		s1 = entNumber.get()
		d = s1.split("/")
		dob = date(int(d[2]), int(d[1]), int(d[0]))
		today = datetime.now().date()
		days = (today - dob)
		age = (today - dob)/timedelta(days=365.24)
		age = round(age,2)
		msg = "age= " + str(age) + "days" + str(days)
		showinfo("Your Age",msg)
	except (ValueError,IndexError):
		showerror("Mistake", 'u need to enter integer only')
		entNumber.delete(0, END)
		entNumber.focus()
	

btnFind = Button(root, text="Find", font=('courier',24,'bold italic'),command=age)
btnFind.pack(pady=10)

root.mainloop()