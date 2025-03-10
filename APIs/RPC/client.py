import requests
import json

payload = json.dumps({"jsonrpc": "2.0", "method": "add", "params": [5, 3], "id": 1})
headers = {'Content-Type': 'application/json'}
response = requests.post("http://localhost:5000", data=payload, headers=headers)
print(response.json())
