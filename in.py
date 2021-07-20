import socket, threading, time #импорт библиотек
import bs4, requests #это для ip
import os as q#ПОдрубаем библиотеку os 
key = 8194#переменая с ключем для шифровки данных ну это мы потом посмотрим 
ips = socket.gethostbyname(socket.gethostname())
shutdown = False
join = False
col = 0
max = 10
#----------------------------НАЧАЛО----------------------------
#позволяет принимать данные другово пользователя 
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
#----------------------------КОНЕЦ----------------------------				
				print(decrypt)
				time.sleep(0.2)
		except:
				pass
host = socket.gethostbyname(socket.gethostname())#переменая которая содержит ip  
port = 0#почему port равен 0 все очень просто клиент будет лишь подключатся к этой сети он не будет её создавать ну как-то так. 
server = (ips,9090)#указываем порт на котором он поднят
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#я уже говорил 
s.bind((host,port))#делаем функцию bind которая будет поключатся к host и port 
s.setblocking(0)#ААААААААА ЭТО ЭТО ПРОСТО О. она нужна для того чтобы не выдовало каких либо ошибок либо это не все  
alias = input("Имя: ")#Вводим значения для переменой alias которая будет содержать имя нашего пользователя и имя как имя
rT = threading.Thread(target = receving, args = ("RecvThread",s))#многопоточность 
rT.start()#запускаем нашу многопоточность вот блин слишком много я чо то объясняю всеровно не кому не чего не понятно
while shutdown == False:#пока клиент не вышел дулаются ледуюшие действия
	if join == False:#если пользователь не присоеденен то отправляется следующие вот тут снизу 
		s.sendto(("[" +alias + "] Вошёл в чат").encode("utf-8"),server)#отправляется сообщение на сервер то что "alias" присоединился к серверу 
		join = True#это то что подключился
	else:
		try:
			message = input()#ввод сообщения самое основное потом мы его будем шинковать
			#а вот тут мы зашифровываем сообщение --НАЧАЛО--
			#---------------------------------------Это я по фикчу пв по фикшу о        
			#crypt = ""
			#for i in message:
			#	crypt += chr(ord(i)^key)
			#message = crypt
			#--КОНЕЦ--
			if message != "":#а тут этот для того чтобы не отправлять пустое сообщение (Здесь мог бы баг)
				s.sendto(("["+alias+"] " + message).encode("utf-8"),server)
			time.sleep(0.2)#(задержка)диопозон между отправкой и получением 
		except:
			s.sendto(("["+alias+"] Покинул чат").encode("utf-8"),server)#сообщение которое отправляется на сервер о том что пользователь покинул чат
			shutdown = True#закрываем соединение 
rT.join()
s.close()
