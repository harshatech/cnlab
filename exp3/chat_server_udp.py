import socket
udp_port=('127.0.0.1',2222)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(udp_port)
while True:
	input=raw_input("server: ")
	if input=="bye" or input=="exit":
		s.sendto(input,('127.0.0.1',2225))
		break
	else:
		s.sendto(input,('127.0.0.1',2225))
	#print "hi"
	data,address=s.recvfrom(1024)
	#print "hi"
	print "client: "+str(data)
