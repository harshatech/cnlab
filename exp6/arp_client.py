import socket
s=socket.socket()
input=raw_input()
s.connect(('127.0.0.1',2220))
input=raw_input("enter ip address:")
s.send(input)
k=s.recv(1024)
print "mac address is : "+k
input=raw_input("enter mac address:")
s.send(input)
k=s.recv(1024)
print "ip address is : "+k
s.close()
