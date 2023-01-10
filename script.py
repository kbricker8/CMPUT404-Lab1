import requests

print(requests.__version__)
print(requests.get('http://www.google.com/'))
r = requests.get('https://raw.githubusercontent.com/kbricker8/Lab1/main/script.py')

print(r.text)