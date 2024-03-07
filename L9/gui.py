#GUI using tkinter


from tkinter import *
from tkinter.messagebox import *

root = Tk()   #used for making the frame
root.title("my fsr gui")
root.geometry("400x200+400+200")      #400x200 --> width,height , +400+200-->x,y
root.resizable(False, False)
root.configure(background= 'sky blue')

def wel():
	showinfo("msg","welcome to the app")


btnWelcome = Button(root, text="welcome", width=10, font=('arial',20,'bold'),command=wel)
btnWelcome.pack(pady=20)

root.mainloop()  #used for staying in program