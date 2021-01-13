import numpy as num

plain=""
f=open("example")
for i in f:
	for j in i:
		if(j.isalnum()):
			if (j.isupper()):
				j=j.lower()
			plain+=j
a=len(plain)
key=raw_input("enter key")
b=len(key)

key1=[]
for i in key:
    key1.append(i)
print(key1)
n1=""
key2=sorted(key1)
print(key2)

n3=""
for i in key1:
    for j in key2:
        if(i==j):
            x=key2.index(j)
            x+=1
            n3+=str(x)

print(n3)

if(a%b!=0):
	c = int(a/b + 1)
else :
	c = int(a/b)	
matrix=''
matrix=num.chararray((c,b))
x=0
for i in range(c):
	for j in range(b):
		if(x<a):
			matrix[i][j]=plain[x]
			x+=1
		else:
			matrix[i][j]='z'
print(matrix)
cipher=''
for k in n3:
	z=int(k)-1
	for i in range(c):
		y=matrix[i][z]
        	cipher += y
print(cipher)
f1=open("new","w").write(cipher)

cipher1=""
f1=open("new")
for i in f1:
	for j in i:
		cipher1 += j

ciphermatrix=num.chararray((c,b))
n=0
for k in n3:
    z=int(k)-1
    for i in range(c):
        ciphermatrix[i][z]=cipher1[n]
        n += 1
print(ciphermatrix)

original=''
for i in range(c):
    for j in range(b):
        q = ciphermatrix[i][j]
        original += q
print(original)

f2=open("original","w").write(original)
