import socket
import requests
import pprint
import json
import pyfiglet

print(pyfiglet.figlet_format("RED--CHIKA",font="slant"))

print("")
print("Ini adalah alat untuk mengecek IP adress buatan RED--CHIKA")
print("")

hostname = input('Masukan nama domain: ')
ip_address = socket.gethostbyname(hostname)

request_url = 'https://geolocation-db.com/jsonp/' + ip_address
response = requests.get(request_url)
geolocation = response.content.decode()
geolocation = geolocation.split("(")[1].strip(")")
geolocation = json.loads(geolocation)
for k,v in geolocation.items():
	pprint.pprint(str(k) + ' : ' + str(v))

