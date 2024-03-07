from tkinter import *
from tkinter.messagebox import *
 
root = Tk()
root.title("Corona Counter")
root.geometry("400x400+400+200")

total_count, death_count, recovery_count = 0, 0, 0

def f1():
	global total_count, death_count, recovery_count
	import socket
	import requests
	import bs4
	import lxml
	
	try:
		google = ("www.google.com",80)
		socket.create_connection(google)

		cn = entCountry.get()

		a1= "https://www.worldometers.info/coronavirus/country/"
		a2= cn + "/"

		web_address = a1 + a2
		

		res = requests.get(web_address)
		print(res)

		s = bs4.BeautifulSoup(res.text, 'lxml')	
		

		data = s.find_all("div", {"class":"maincounter-number"})
		

		total_count = data[0].find('span').text
		death_count = data[1].find('span').text
		recovery_count = data[2].find('span').text

		

		msg = "total count" + total_count + "\ndeath count" + death_count + "\nrecovery count" + recovery_count
		showinfo("count",msg)

		


	except OSError as e:
		print("issue ",e)
	except Exception as e:
		showerror("Error","entry valid country")
		entCountry.delete(0, END)
		entCountry.focus()


def f2():
	global total_count, death_count, recovery_count
	import matplotlib.pyplot as plt
	l2 = ['active','death','recovery']

	total_count = total_count.replace(",","")
	death_count = death_count.replace(",","")
	recovery_count = recovery_count.replace(",","")

	l1 = [float(total_count),float(death_count),float(recovery_count)]

	plt.pie(l1, labels=l2, autopct='%0.1f%%')
	plt.axis('equal')
	plt.show()




lblCountry = Label(root, text="enter country name ",font=('arial', 18, 'bold'))
entCountry = Entry(root, bd=5,font=('arial', 18, 'bold') )
btnGet = Button(root, text="Get Count",font=('arial', 18, 'bold') , command=f1)
btnChart = Button(root, text="Pie Chart",font=('arial', 18, 'bold'),command=f2)

lblCountry.pack(pady=10)
entCountry.pack(pady=10)
btnGet.pack(pady=10)
btnChart.pack(pady=10)
root.mainloop()
