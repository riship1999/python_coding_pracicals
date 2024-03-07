from tkinter import *
from tkinter.messagebox import *

win = Tk()
win.title("What Next??")
win.geometry("500x400+400+200")

def f1():
	ch = sel.get()
	if ch == 1:
		msg = "Job"
	elif ch == 2:
		msg = "Ms"
	elif ch == 3:
		msg = "mba"
	elif ch == 4:
		msg = "Mtech"
	else:
		msg = "Submit"
	showinfo("Choice",msg)

sel = IntVar()
sel.set(1)
rbJob = Radiobutton(win, text='Job', font=('times new roman',28,'italic'),variable=sel,value=1)
rbMs = Radiobutton(win, text='M S', font=('times new roman',28,'italic'),variable=sel, value=2)
rbMba = Radiobutton(win, text='M B A', font=('times new roman',28,'italic'),variable=sel, value=3)
rbMTech = Radiobutton(win, text='M tech', font=('times new roman',28,'italic'),variable=sel, value=4)
btnSubmit = Button(win, text="Submit",font=('times new roman',28,'italic'),command=f1)


rbJob.grid(sticky='W')
rbMs.grid(sticky='W')
rbMba.grid(sticky='W')
rbMTech.grid(sticky='W')
btnSubmit.grid()
win.mainloop()