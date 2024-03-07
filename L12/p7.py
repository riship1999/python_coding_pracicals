import socket
import requests
import bs4
import lxml

try:
	google = ("www.google.com",80)
	socket.create_connection(google)
	print("connected")

	res = requests.get("https://www.worldometers.info/coronavirus/country/india/")
	print(res)

	s = bs4.BeautifulSoup(res.text, 'lxml')	
	#print(s)

	data = s.find_all("div", {"class":"maincounter-number"})
	print(data)

	total_count = data[0].find('span').text
	death_count = data[1].find('span').text
	recovery_count = data[2].find('span').text

	print("total count", total_count)
	print("death count", death_count)
	print("recovery count", recovery_count)


except OSError as e:
	print("issue ",e)


