# wapp3 to connect to openweathermap.org and get some info
import requests
import socket
try:
	google = ("www.google.com", 80 )
	socket.create_connection(google)
	print("connected")

	city = input("enter city name ")
	a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&appid=c6e315d09197cec231495138183954bd"
	a3 = "&q=" + city 

	web_address = a1 + a2 + a3
	res = requests.get(web_address)
	print(res)

	data = res.json()
	print(data)

	# write code to get temp
	main = data['main']
	print("main--> ",main)
	t = main['temp']
	print("temperature1", t)

	temp2 = data['main']['temp']
	print("temp2 ",temp2)

except OSError as e:
	print("issue ", e)
