import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',5553))
n=raw_input()
s.sendto(n,('127.0.0.1',5555))
k,addr=s.recvfrom(1024)
print k
n=raw_input()
s.sendto(n,('127.0.0.1',5555))
k,addr=s.recvfrom(1024)
print k

