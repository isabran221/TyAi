import requests

response = requests.get("http://127.0.0.1:5000/sumar?a=10&b=5")
print(response.json())
