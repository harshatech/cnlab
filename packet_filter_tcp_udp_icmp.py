import socket,sys,threading,time
from struct import *
s1=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_TCP)
s2=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_UDP)
s3=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
count=0
tcp=0
icmp=0
udp=0
def printvalues():
        global udp
        global tcp
        global icmp
        print "udp :"+str(udp)+" tcp :"+str(tcp)+" icmp:"+str(icmp)
def tcpcount():
        global count
        global tcp
        while True:
                if count>200:
                        printvalues()
                        sys.exit()
                packet=s1.recvfrom(65565)
                print packet
                count+=1
                tcp+=1
#               time.sleep(1)

def udpcount():
        global count
        global udp
        while True:
                if count>200:
                        printvalues()
                        sys.exit()
                packet=s2.recvfrom(65565)
                print packet
                count+=1
                udp+=1
#               time.sleep(1)

def icmpcount():
        global count
        global icmp
        while True:
                if count>200:
                        printvalues()
                        sys.exit()
                packet=s3.recvfrom(65565)
                print packet
                count+=1
                icmp+=1
#               time.sleep(1)
lock=threading.Lock()
lock.acquire()
threading.Thread(target=tcpcount).start()
threading.Thread(target=udpcount).start()
threading.Thread(target=icmpcount).start()
print "hi"
lock.release()

#while count<200:
#       count+=1
#       packet=s.recvfrom(65565)
#       print packet
#       packet=packet[0]
#       ip_header=packet[0:20]
#       iph = unpack('!BBHHHBBH4s4s' , ip_header)
#       protocol=iph[6]
#       print protocol
#       p=int(protocol)
#       if p==1:
#               icmp+=1
#       elif p==6:
#               tcp+=1
#       elif p==17:
#               udp+=1
        #threading.Thread(target=tcpcount).start()
        #threading.Thread(target=udpcount).start()
        #threading.Thread(target=icmpcount).start()
