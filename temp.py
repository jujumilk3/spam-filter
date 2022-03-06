import requests

url = 'https://goo.gl/88srfV'
session = requests.Session()
# response = session.head(url, allow_redirects=True)
response = requests.get('http://localhost:8000/reredirect')
print(response.url)





"""
samples:
1. 멀쩡한거 https://goo.gl/88srfV
2. 맛탱이간거 bit.ly/silly

"""
