import requests
import json
request_server=requests.get("http://54.67.55.103:3000/api/getclasstoken/1/")
j = json.loads(request_server.text)
token=j[0]['token']
print token