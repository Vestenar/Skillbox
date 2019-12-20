import requests

for i in range(10):
    print(requests.post('http://127.0.0.1:5000/auth', json={'login': 'admin', 'password': '12345'}).status_code)
