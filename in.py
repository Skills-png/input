import sys
from socket import socket, AF_INET, SOCK_DGRAM

SERVER_IP   = '172.16.51.14'
PORT_NUMBER = 5000
SIZE = 1024
print ("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))

mySocket = socket( AF_INET, SOCK_DGRAM )

while True:
	
        mySocket.sendto(input().encode('utf8'),(SERVER_IP,PORT_NUMBER))
sys.exit()
