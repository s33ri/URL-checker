import requests
import re
import sys

with open(sys.argv[1]) as f:
    content = f.readlines()
content = [line.strip() for line in content]
i = 0
while i < len(content):
    url = 'https://' + str(content[i])
    if re.match(r'[\w.]+[.][\w.]+',str(content[i])):
        try:
            req = requests.get(url, allow_redirects=False)
        except requests.exceptions.RequestException as err:
            print ("Connection error:", err)
            i = i + 1
            continue
    else:
        print('Wrong input at ', url)
        i = i+1
        continue
    if req.status_code in [200, 201, 202, 100, 101]:
        print('URL is accessible', url)
    elif req.status_code in [500, 404, 501, 502, 503, 504]:
        print('Server Error', url)
    elif req.status_code in [301, 302, 303, 304]:
        print(url, ' is Redirecting to other domain')
    elif req.status_code in [403]:
        print('Access forbidden', url)
    elif req.status_code in [405]:
        print('Method not allowed', url)
    else:
        print('Unrecognized Response', url)
    i = i + 1