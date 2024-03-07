#wapp to check internet

import socket
try:
	google = ("www.google.com", 80)  #(domain,port)
	socket.create_connection(google)
	print("connected")
except OSError as e:
	print("Issue ",e)