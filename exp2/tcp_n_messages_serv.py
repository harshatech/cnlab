import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',2222))
s.listen(5)
client,address=s.accept()
while True:
	str=client.recv(1024)
	temp=''
	out=''
	for k in str:
		if(ord(k)>=97 and ord(k)<=122):
			temp=chr(ord(k)-32)
		else:
			temp=k
		if out=='':
			out=temp				
		else:
			out+=temp
	client.send(out)

