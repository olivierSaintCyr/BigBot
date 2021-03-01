import requests

BASE = "http://localhost:5001/"
response = requests.get(BASE, {"_id": "799761080720687164"})
print(response.json())
response_not_setup = requests.get(BASE, {"_id": "799761080720687160"})
print(response_not_setup.json())