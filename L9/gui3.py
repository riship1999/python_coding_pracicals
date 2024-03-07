from tkinter import *
from tkinter.messagebox import *

root = Tk()   #used for making the frame
root.title("color me")
root.geometry("400x400+400+200")      #400x200 --> width,height , +400+200-->x,y
root.resizable(False, False)


def c(num):
	if num == 1:
		root.configure(background= 'red')
	elif num == 2:
		root.configure(background= 'blue')
	else:
		root.configure(background= 'green')
	
		


btnRed = Button(root, text="Red", width=10, font=('arial',20,'bold'),command=lambda:c(1))
btnRed.pack(pady=20)

btnBlue = Button(root, text="Blue", width=10, font=('arial',20,'bold'),command=lambda:c(2))
btnBlue.pack(pady=20)

btnGreen = Button(root, text="Green", width=10, font=('arial',20,'bold'),command=lambda:c(3))
btnGreen.pack(pady=20)


root.mainloop()  #used for staying in program