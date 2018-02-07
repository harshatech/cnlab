import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',5554))
while True:
	n=input()
	s.sendto(str(n),('127.0.0.1',5555))
	data,addr= s.recvfrom(1024)
	print data
