def euclidian(k1,n):
	
	r1=n
	r2=k1
	t1=0
	t2=1
	while(r2>0):
		q=r1/r2
		r=r1%r2
		r1,r2=r2,r
		t=t1 - (q*t2)
		t1,t2=t2,t
	if(r1==1):
		new=t1 % 256
		return new
	else:
		print("NOT POSSIBLE by key k1")
		exit()

def encrypt(i,k1,k2):
	t= (i*k1) % 256
	ci= (t+k2) % 256
	return chr(ci)

def decrypt(i,k1,k2):
	t= (i-k2) % 256
	pl= (t*k1) % 256
	return chr(pl)

plain=''
f=open("example.txt")
for i in f:
	for j in i:
		plain += j

k1=int(input("enter k1 : "))
k2=int(input("enter k2 : "))
n=256
inverse=euclidian(k1,n)
print(inverse)

cipher=''
for i in plain:
	cipher += encrypt(ord(i),k1,k2)
print(cipher)
f1=open("cipher.txt","w").write(cipher)

print("====================")
cipher1=''
f1=open("cipher.txt")
for i in f1:
	for j in i:
		cipher1 += j


original=''
for i in cipher1:
	original += decrypt(ord(i),inverse,k2)
print(original)
f1=open("original.txt","w").write(original)
