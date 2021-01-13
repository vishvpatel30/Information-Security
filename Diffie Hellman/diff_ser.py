import random
import socket	               # inport socket module
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          # create a socket object

port = 12345					# Reserve a port for your service
s.bind(('',port))           # bind to the port, permit connection from any node in connection 
	
s.listen(5)         #now wait for client connection
while True:
	c, addr = s.accept()		#Establish connection with client.
	print 'Got connection from', addr
	
	p=c.recv(1024)
	print 'received p ->  ' + p + '\n'
	
	msg = raw_input("enter a msg -> ")
	c.send(msg)
	print("\n")
	
	g=c.recv(1024)
	print 'received g ->  ' + g + '\n'

	msg = raw_input("enter a msg -> ")
	c.send(msg)
	print("\n")
	
	p=int(p)
	g=int(g)
	
	y=random.randint(1,p)
	r2=g**y % p
	print(r2)

	r1=c.recv(1024)
	print 'received r1 ->  ' + r1 + '\n'

	msg = raw_input("enter a msg -> ")
	c.send(msg)
	print("\n")

	c.send(str(r2))

	msg = c.recv(1024)
	print 'received ->  ' + msg +  '\n'

	r1=int(r1)
	key=r1**y % p
	print(key)
			
c.close()            # close the connection  	


