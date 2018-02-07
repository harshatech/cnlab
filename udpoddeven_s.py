import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1",5555))
while True:
	data,address=s.recvfrom(1024)
	data=int(data)
	if data%2==0:
		s.sendto('even',('127.0.0.1',5554))
	else:
		s.sendto('odd',('127.0.0.1',5554))

