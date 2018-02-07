import xmlrpclib
proxy = xmlrpclib.ServerProxy("http://localhost:8888/")
print (proxy.get_date())
