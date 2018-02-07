p=input()
q=input()
e=input()
d=1
s=0
n=p*q
phi=(p-1)*(q-1)
while(s!=1):
	s=(d*e)%phi
	d+=1
d-=1
print d
data=raw_input()
print "encrypt"
enc=[]
for k in data:
	l=ord(k)
	c=1
	for m in range(0,e):
		c*=l
		c%=n
	c%=n
	enc.append(c)
print enc		
print "decrypt"
dec=[]
for k in enc:
	c=1
	for l in range(0,d):
		c*=k
		c%=n
	c%=n
	dec.append(chr(c))
print dec
str=' '
for k in dec:
	str+=k
print str[1:]
