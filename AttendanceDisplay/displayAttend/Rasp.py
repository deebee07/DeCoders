import requests
request_server=requests.post("http://54.67.55.103:3000/api/getclasstoken/1/")
print(request_server.text)
time.sleep(5)