import requests as re
import sys

def loop():
  for word in sys.stdin:
    req = re.get(url=f"https://{domain}/{word}")
    if req.status_code == 404:
	loop()
    else:
	data = req.json
    	print(data)
	print(req.status_code)
	print(word)
loop()
