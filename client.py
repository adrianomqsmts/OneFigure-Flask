import requests

r = requests.post('http://localhost:5000/', data={'name': 'teste', 'password': 'teste'})
print(r.json())
