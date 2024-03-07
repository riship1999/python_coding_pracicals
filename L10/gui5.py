from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Even Odd")
root.geometry("400x400+500+200")

lb1Number = Label(root, text="Enter number", font=('courier',24, 'bold italic'))
lb1Number.pack(pady=10)

entNumber = Entry(root, bd=5, font=('courier',24,'bold italic'))
entNumber.pack(pady=10)
entNumber.focus()

def eo():
	try:
		s1 = entNumber.get()
		n1 = int(s1)
		if n1 % 2 == 0:
			res = "even"
		else:
			res = "odd"
		showinfo("Result",res)
	except ValueError:
		showerror("Mistake", 'u need to enter integer only')
		entNumber.delete(0, END)
		entNumber.focus()
	

btnFind = Button(root, text="Find", font=('courier',24,'bold italic'),command=eo)
btnFind.pack(pady=10)

root.mainloop()
