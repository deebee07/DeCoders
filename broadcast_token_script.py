import requests
import json
request_server=requests.get("http://54.67.55.103:3000/api/getclasstoken/1/")
j=json.loads(request_server.text)
token=j[0]['token']
print token

import os
import glob
import time
import RPi.GPIO as GPIO
from bluetooth import *

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)



server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service( server_sock, "AquaPiServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ], 
#                   protocols = [ OBEX_UUID ] 
                    )
while True:          
	print "Waiting for connection on RFCOMM channel %d" % port

	client_sock, client_info = server_sock.accept()
	print "Accepted connection from ", client_info

	try:
	        data = client_sock.recv(1024)
        	if len(data) == 0: break
	        print "received [%s]" % data

		if data == 'temp':
			data = str(token) +'!'
		
		else:
			data = 'WTF!' 
	        client_sock.send(data)
		print "sending [%s]" % data

	except IOError:
		pass

	except KeyboardInterrupt:

		print "disconnected"

		client_sock.close()
		server_sock.close()
		print "all done"

		break
