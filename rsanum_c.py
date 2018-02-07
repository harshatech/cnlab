import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
p=input("enter p:")
q=input("enter q:")
n=p*q
phi=(p-1)*(q-1)
e=input("enter e:")
s1=0
d=1
while s1!=1:
	s1=(d*e)%phi
	d+=1
d-=1
pub_key=str(e)+"-"+str(n)
s.connect(('127.0.0.1',5555))
s.send(pub_key)
k=s.recv(1024)
print "secret number received : "+k
k=int(k)
c=1
for l in range(0,d):
	c*=k
	c%=n
c%=n
print "original number : "+str(c)