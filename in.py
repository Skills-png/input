import socket, threading, time
import bs4, requests 
import os as q
key = 8194
ips = socket.gethostbyname(socket.gethostname())
shutdown = False
join = False
col = 0
max = 10
def receving (name, sock):
	while not shutdown:
		try:
			while True:
				data, addr = sock.recvfrom(1024)
				decrypt =""; k = False
				for i in data.decode("utf-8"):
					if i == ":":
						k = True
						decrypt += i 
					elif k == False or i == " ":
						decrypt += i
					else:
						decrypt += chr(ord(i)^key)
			
				print(decrypt)
				time.sleep(0.2)
		except:
				pass
host = socket.gethostbyname(socket.gethostname())
port = 0
server = (ips,9090)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
s.bind((host,port)) 
s.setblocking(0)
alias = input("Имя: ")
rT = threading.Thread(target = receving, args = ("RecvThread",s))
rT.start()
while shutdown == False:
	if join == False:
		s.sendto(("[" +alias + "] is").encode("utf-8"),server)
		join = True
	else:
		try:
			message = input()
			if message != "":
				s.sendto(("["+alias+"] " + message).encode("utf-8"),server)
			time.sleep(0.2)
		except:
			s.sendto(("["+alias+"] close").encode("utf-8"),server)
			shutdown = True
rT.join()
s.close()
