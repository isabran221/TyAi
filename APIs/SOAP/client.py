from zeep import Client
client = Client('http://localhost:8000/?wsdl')
print(client.service.greet('Juan', 25))