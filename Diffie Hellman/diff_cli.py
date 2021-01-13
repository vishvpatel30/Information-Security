import math
import random


def isgen(g,p):
	r1=p
	r2=g
	while(r2>0):
		q=r1/r2
		r=r1%r2
		r1,r2=r2,r
	if(r1==1):
		return True
	return g

def isprime(p):	
	for i in range(2,int(math.sqrt(p)+1)):
		if p%i==0:
			return False
	return p


flag=0
while flag==0:
	p=random.randint(0,100)
	if isprime(p):
		flag=1
		print("p ->" + p)

temp=0
while temp==0:
	g=random.randint(1,p-2)
	if isgen(g,p):
		temp=1
		print("g ->" + g)

x=random.randint(1,p)

import socket	               # inport socket module
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          # create a socket object

port = 12345	
s.connect(("10.30.7.88",port))


s.send(str(p))

msg = s.recv(1024)
print 'received ->  ' + msg +  '\n'

s.send(str(g))

msg = s.recv(1024)
print 'received ->  ' + msg +  '\n'

r1=g**x % p
print(r1)

s.send(str(r1))

msg = s.recv(1024)
print 'received ->  ' + msg +  '\n'

r2=s.recv(1024)
print 'received r2 ->  ' + r2 + '\n'

msg = raw_input("enter a msg -> ")
s.send(msg)
print("\n")

r2=int(r2)
key=r2**x % p
print(key)



