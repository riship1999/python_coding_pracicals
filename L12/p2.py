#wapp to connect to ipinfo.io and get some info

import requests
import socket
try:
	google = ("www.google.com", 80)
	socket.create_connection(google)
	print("connected")
	
	res = requests.get("http://ipinfo.io/")
	print(res)

	data = res.json()
	print(data)

	city_name = data['city']
	print(city_name)

	location = data['loc']
	print(location)
	l = location.split(",")
	print("lat", l[0], "long", l[1])



except OSError as e:
	print("issue", e)