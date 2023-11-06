import requests

endpoint = "http://127.0.0.1:8000/api"
response = requests.get(endpoint, json = {'query': 'Hello Dave'})
print(response.json())
print(response.status_code)