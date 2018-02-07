import socket
s=socket.socket()
n=int(raw_input("enter n:"))
s.connect(('127.0.0.1',2222))
for k in range(0,n):
	input=raw_input()
	#s.connect(('127.0.0.1',2222))
	s.send(input)
	k=s.recv(1024)
	print k
