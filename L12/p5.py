import socket
import requests
try:
	google = ("www.google.com", 80)
	socket.create_connection(google)
	print("connected")

	movie_name = input("enter movie name to search ")

	a1 = "http://www.omdbapi.com/?"
	a2 = "&apikey=b88add31"
	a3 = "&s=" + movie_name

	web_address = a1 + a2 + a3
	res = requests.get(web_address)
	print(res)
	
	data = res.json()
	print(data)
	
	search = data['Search']
	print(search)

	for s in search:
		print("$" * 30)
		title = s['Title']
		print("Title -->", title)
		year = s['Year']
		print("Year --> ", year)
		poster = s['Poster']
		print("Poster --> ",poster)
		
	#write code to download poster
	if poster != 'N/A':
		res = requests.get(poster)
		file_name = title + ".jpg"
		f = None
		try:
			f = open(file_name, "wb")
			f.write(res.content)
		except Exception as e:
			print("Issue ",e)
		finally:
			if f is not None:
				f.close()




except OSError as e:
	print("issue", e)
except KeyError as e:
	print("check movie name ", e)