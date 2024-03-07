from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("square calci")
root.geometry("500x300+400+200")

def sqr():
	try:
		s1 = entNumber.get()
		n1= float(s1)
		sq = n1 * n1
		showinfo("Square",sq)
	except ValueError:
		showerror("mistake",'u need to enter integer')
		entNumber.delete(0,END)
		entNumber.focus()
		
		


lblNumber = Label(root, text="enter number", font=('arial',18,'bold'))
entNumber = Entry(root, bd=5, font=('arial',18,'bold'))
entNumber.focus()
btnFind = Button(root, text="Find",font=('arial',18,'bold'),command=sqr)

lblNumber.place(x=20, y=20)
entNumber.place(x=200,y=20)
btnFind.place(x=150,y=80)

root.mainloop()