import socket, threading, time, bs4, requests 
key = 8194
shutdown = False
join = False
host = socket.gethostbyname(socket.gethostname())
server = (socket.gethostbyname(socket.gethostname()), 9090)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host, 0))
s.setblocking(0) 
def receving(name, sock):
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
rT = threading.Thread(target = receving, args = ("RecvThread",s))
rT.start()
while shutdown == False:
	if join == False:
		join = True
	else:
		try:
			message = input()
			if message != "":
				s.sendto((message).encode("utf-8"),server)
			time.sleep(0.2)
		except:
			shutdown = True
rT.join()
s.close()
