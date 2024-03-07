from tkinter import *
from tkinter.messagebox import *
from webbrowser import *
from datetime import *

root = Tk()
root.title("D n t App")
root.geometry("400x400+400+200")
root.configure(background='sky blue')

def da():
	d = datetime.now().date()
	showinfo("Date", d)

def ti():
	t = datetime.now().time()
	showwarning("Time", t)

def da_ti():
	dt = datetime.now()
	showerror("Dnt", dt)

def vi():
	open("www.google.com")
	

btnDate = Button(root, text="Date", width=12, font=('arial',16,'bold'),command=da)
btnTime = Button(root, text="Time", width=12, font=('arial',16,'bold'), command=ti)
btnDateTime = Button(root, text="Date And Time", width=12, font=('arial',16,'bold'), command=da_ti)
btnVisitUs = Button(root, text="Visit Us", width=12, font=('arial',16,'bold'), command=vi)

btnDate.pack(pady=8)
btnTime.pack(pady=8)
btnDateTime.pack(pady=8)
btnVisitUs.pack(pady=8)

root.mainloop()