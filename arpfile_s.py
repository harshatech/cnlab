import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ipmac={}
f=open("arp.txt",'r')
for k in f.readlines():
	if ',' not in k:
		continue
	l=k.split(',')
	ipmac[l[0]]=l[1][:-1]
#print ipmac

s.bind(('127.0.0.1',5555))
k,addr=s.recvfrom(1024)
s.sendto(ipmac[k],('127.0.0.1',5553))
k,addr=s.recvfrom(1024)
for l in ipmac.keys():
	if ipmac[l]==k:
		s.sendto(l,('127.0.0.1',5553))

s.close()
