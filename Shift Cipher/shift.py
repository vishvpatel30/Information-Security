import numpy as np
import math


def prime(a):
	for i in range(int(math.sqrt(a)) + 1):
		if (a % (i + 1) == 0):
			return 1
	return 0


def reform(b, key):
	a = (b - key) % 256
	return (a)


def gcd(a, b):
	t1 = 0
	t2 = 1
	r1 = b
	r2 = a

	while (r2 != 0):
		q = int(r1 / r2)
		r = r1 % r2
		r1 = r2
		r2 = r

		t = t1 - (q * t2)
		t1 = t2
		t2 = t
	return (r1)


def freq(old):
	D = {}
	internet = " etaoinsrhdlucmfywgpbvkxqjz0123456789"
	for i in old:
		try:
			D[i] = D[i] + 1
		except:
			D[i] = 1
	maxn = 0
	maxc = ""
	for i in D:
		if (D[i] > maxn):
			maxn = D[i]
			maxc = i
	print("max is = " + str(maxc) + "-------------------------------------------------")

	for i in internet:
		a = ord(i)
		b = ord(maxc)
		key = (b - a) % 256
		print("key = " + str(key) + "------------------------------------------------------------------")
		new = ""
		for j in old:
			a = ord(j)
			b = chr(reform(a, key))
			new += b
		return (new)
def number(p,a):
	abc="abcdefghijklmnopqrstuvwxyz"
	for i in range(len(abc)):
		if(abc[i]==p[a]):
			return i

def string(z):
	abc = "abcdefghijklmnopqrstuvwxyz"
	for i in range(len(abc)):
		if(i==z):
			return abc[i]


plain=input("Enter the plain text : ")
key=input("Enter the key : ")

pl=len(plain)
ke=len(key)

cipher=""
pl_a = 0
while (pl_a < pl):
	ke_b = 0
	while (ke_b < ke and pl_a < pl):
		if plain[pl_a] is " ":
			cipher += " "
			pl_a += 1
		enc_num = number(plain,pl_a) + number(key,ke_b)
		enc = enc_num % 26
		cipher += string(enc)
		ke_b += 1
		pl_a += 1
print(cipher)



ci=len(cipher)
ke=len(key)
a=input("do you know key")
if(a=="yes"):
	original=""
	pl_a = 0
	while (pl_a < ci):
		ke_b = 0
		while (ke_b < ke and pl_a < ci):
			if cipher[pl_a] is " ":
				original += " "
				pl_a += 1
			dec_num = number(cipher,pl_a) - number(key,ke_b)
			dec = dec_num % 26
			original += string(dec)
			ke_b += 1
			pl_a += 1
	print(original)


elif(a=="illegal"):

	l = []
	a = 0
	gc = 0
	for i in range(len(cipher)-2):
		a = cipher[i:i+3]
		diff = cipher[i+3:].find(a) + 3
		l.append(diff)
		if(diff != 2):
			print(a)
		if(a == 0 and diff!=2 and prime(diff)==1):
			gc = diff
		elif(diff != 2 and prime(diff)==1):
			gc = gcd(gc,diff)
	print(gc)
	print(l)
	print("------------------------------------------------------")
	while(len(cipher)%gc!=0):
		cipher+="*"
	a = np.chararray([gc,len(cipher)/gc])
	a[:] = "+"
	z = 0
	for j in range(len(a[0])):
		for i in range(len(a)):
			a[i][j] = cipher[z]
			z+=1
	ans = "no"
	while(ans!="yes"):
		b = np.chararray([gc,len(cipher)/gc])
		b[:] = "+"
		for i in range(gc):
			txt = ""
			for j in range(len(a[0])):
				txt += a[i][j]
			txt = freq(txt)
			for j in range(len(a[0])):
				b[i][j] = txt[j]
		txt = ""
		for j in range(len(b[0])):
			for i in range(len(b)):
				txt += b[i][j]
		print(b)
		ans = input("is it the text")