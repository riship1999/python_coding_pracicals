import socket
import requests
import bs4
import lxml

try:
	google = ("www.google.com",80)
	socket.create_connection(google)
	print("connected")

	res = requests.get("https://www.brainyquote.com/quote_of_the_day")
	print(res)
	
	s = bs4.BeautifulSoup(res.text, 'lxml')
	print(s)

	data = s.find('img', {"class":"p-qotd"})
	print("data ",data)
	
	quote = data['alt']
	print("quote--> ",quote)
	
	#code to download image
	image_url ="https://www.brainyquote.com" + data["data-img-url"]
	f = None
	
	try:
		f = open("im.jpg", "wb")
		res = requests.get(image_url)
		f.write(res.content)
	except Exception as e:
		print(e)
	finally:
		if f is not None:
			f.close()	

except OSError as e:
	print("issue ",e)