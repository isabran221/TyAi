from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class SoapService(ServiceBase):
    @rpc(Unicode, Integer, _returns=Unicode)
    def greet(ctx, name, age):
        return f"Hola {name}, tienes {age} años."

app = Application([SoapService], 'soap.example',
                  in_protocol=Soap11(), out_protocol=Soap11())

from wsgiref.simple_server import make_server
server = make_server('0.0.0.0', 8000, WsgiApplication(app))
server.serve_forever()
