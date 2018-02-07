import xmlrpclib
import time
from SimpleXMLRPCServer import SimpleXMLRPCServer
def get_date():
 	return time.strftime("%H %M %S")

server=SimpleXMLRPCServer(('localhost',8888))
server.register_function(get_date,"get_date")
server.serve_forever()