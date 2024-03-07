#wapp to download image

import socket 
import requests
try:
	google = ("www.google.com",80)
	socket.create_connection(google)
	print("connected")

	img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Shaqi_jrvej.jpg/250px-Shaqi_jrvej.jpg"
	res = requests.get(img_url)
	print(res)
	
	file_name = "nature.jpg"
	f = None
	try:
		f = open(file_name, "wb")
		f.write(res.content)
	except Exception as e:
		print("download issue ",e)
	finally:
		if f is not None:
			f.close()
except OSError as e:
	print("issue ", e )