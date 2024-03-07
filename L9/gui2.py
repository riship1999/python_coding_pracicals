#color me

from tkinter import *
from tkinter.messagebox import *

root = Tk()   #used for making the frame
root.title("Color Me")
root.geometry("300x400+400+200")      #400x200 --> width,height , +400+200-->x,y
root.resizable(False, False)
root.configure(background= 'white')

def RED():
	root.configure(background= 'red')

def BLUE():
	root.configure(background= 'blue')

def GREEN():
	root.configure(background= 'green')
	


btnRed = Button(root, text="Red", width=10, font=('arial',20,'bold'),command=RED)
btnRed.pack(pady=20)

btnBlue = Button(root, text="Blue", width=10, font=('arial',20,'bold'),command=BLUE)
btnBlue.pack(pady=20)

btnGreen = Button(root, text="Green", width=10, font=('arial',20,'bold'),command=GREEN)
btnGreen.pack(pady=20)

root.mainloop()  #used for staying in program