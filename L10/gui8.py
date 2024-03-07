from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Pizza Order")
root.geometry("400x400+500+200")

def order():
	toppings = ""
	if t.get() == 1:
		toppings = toppings + " Tomato "
	if c.get() == 1:
		toppings = toppings + " Cheese "
	if o.get() == 1:
		toppings = toppings + " Onion "
	if j.get() == 1:
		toppings = toppings + " Jalapeno "
	showinfo("Order", toppings)


t , c , o , j = IntVar() , IntVar() , IntVar(), IntVar()

cbTomato = Checkbutton(root, text="Tomato", font=("arial",18,"bold"),variable=t)
cbCheese = Checkbutton(root, text="Cheese", font=("arial",18,"bold"),variable=c)
cbOnion = Checkbutton(root, text="Onion", font=("arial",18,"bold"),variable=o)
cbJalapeno = Checkbutton(root, text="Jalapeno", font=("arial",18,"bold"),variable=j)
btnOrder = Button(root, text="Submit", font=("arial",18,"bold"),command=order)

cbTomato.grid(sticky="W")
cbCheese.grid(sticky="W")
cbOnion.grid(sticky="W")
cbJalapeno.grid(sticky="W")
btnOrder.grid()
root.mainloop()


