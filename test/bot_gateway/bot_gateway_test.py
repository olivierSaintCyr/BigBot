import requests

BASE = "http://localhost:5000/"

query_good = {"server_id":"799761080720687164", "service":"echo_test"}
query_not_sub = {"server_id":"799761080720687164", "service":"not_a_service"}
query_server_not_setup = {"server_id":"799761080720687160", "service":"echo_test"}
response = requests.get(BASE, query_good)
print(response.json())
response = requests.get(BASE, query_not_sub)
print(response.json())
response = requests.get(BASE, query_server_not_setup )
print(response.json())