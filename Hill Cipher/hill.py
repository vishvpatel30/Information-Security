import numpy as num
import math as ma





def inverse(n,a):
	r1,r2=n,a
	t1,t2=0,1
	while(r2>0):
		q=int(r1/r2)
		r=r1%r2
		t=t1-(q*t2)
		r1,r2=r2,r
		t1,t2=t2,t
	if(r1==1):
		return t1
	else:
		exit(" matrix determinant zero")

def minor(matrix,x,y,c):
	minor_list=[]
	for i in range(c):
		for j in range(c):
			if(i!=x and j!=y):
				minor_list.append(matrix[i][j])
	
	matrix_minor=num.ndarray(shape=(c-1,c-1),dtype="int")
	k=0
	for i in range(c-1):
		for j in range(c-1):
			matrix_minor[i][j]=minor_list[k]
			k+=1
	det_minor=num.linalg.det(matrix_minor)
	return round(det_minor)


def cofactor(matrix,c):
	matrix_cof=num.ndarray(shape=(c,c),dtype="int")
		
	for i in range(c):
		for j in range(c):
			matrix_cof[i][j]=int(((-1)**(i+j)) * (minor(matrix,i,j,c)))
	return matrix_cof.T


plain=""
string="abcdefghijklmnopqrstuvwxyz"
f=open("example.txt")
for i in f :
	for j in i:
		plain += j

pl=len(plain)
print(pl)
print(plain)
key=raw_input("Enter the key : ")
a=len(key)
b=ma.sqrt(a)
c=int(ma.ceil(b))

while(pl%c!=0):
	plain += "z"
	pl=len(plain)
print(plain)
x=q=n=0
matrix=num.chararray((c,c))
z=c*c
while(x<z):
	for i in range(c):
		for j in range(c):
			if(n<a):
				matrix[i][j]=key[n]
				n+=1
			else:
				matrix[i][j]=string[q]
				q+=1
			x+=1
print(matrix)

matrix_num=num.ndarray(shape=(c,c),dtype="int")
for i in range(c):
	for j in range(c):
		p=matrix[i][j]
		matrix_num[i][j]=ord(p)%256
print(matrix_num)




new=num.chararray((c,1))
new_num=num.ndarray(shape=(c,1),dtype="int")
orig=num.chararray((c,1))
cipher=""


ab=0
while(ab<pl):
	for i in range(c):
		for j in range (1):
			new[i][j]=plain[ab]
			ab+=1
	
	for i in range (c):
		for j in range(1):
			q=new[i][j]
			if q is "":
				q=" "
			new_num[i][j]=ord(q)%256

	orig=num.dot(matrix_num,new_num)%256
	
	for i in range(c):
		for j in range(1):
			z=orig[i][j]
			a=chr(z)
			cipher += a
	
print(cipher)
f1=open("new.txt","w").write(cipher)




print("============================================================================")


cipher1=""
f=open("new.txt")
for i in f :
	for j in i:
		cipher1 += j


key=raw_input("Enter the key :  ")
a=len(key)
b=ma.sqrt(a)
c=int(ma.ceil(b))
ci_len=len(cipher1)


x=q=n=0
matrix1=num.chararray((c,c))
z=c*c
while(x<z):
	for i in range(c):
		for j in range(c):
			if(n<a):
				matrix1[i][j]=key[n]
				n+=1
			else:
				matrix1[i][j]=string[q]
				q+=1
			x+=1
print(matrix)

matrix1_num=num.ndarray(shape=(c,c),dtype="int")
for i in range(c):
	for j in range(c):
		p=matrix1[i][j]
		matrix1_num[i][j]=ord(p)%256

det=num.linalg.det(matrix1_num)
det_key=int(round(det)%256)


inver=inverse(256,det_key)%256


matrix_adj=num.ndarray(shape=(c,c),dtype="int")
matrix_adj=cofactor(matrix1_num,c)%256

inverse_matrix=(matrix_adj*inver)%256
print("inverse_matrix")
print(inverse_matrix)



cipher_matrix=num.chararray((c,1))
ciphermatrix_num=num.ndarray(shape=(c,1),dtype="int")
orig=num.chararray((c,1))


original_plain=""

ab=0
while(ab<ci_len):
	for i in range(c):
		for j in range (1):
			cipher_matrix[i][j]=cipher[ab]
			ab+=1
	
	for i in range (c):
		for j in range(1):
			q=cipher_matrix[i][j]
			if q is "":
				q=" "
			ciphermatrix_num[i][j]=ord(q)%256
	
	orig=num.dot(inverse_matrix,ciphermatrix_num)%256

	for i in range(c):
		for j in range(1):
			z=orig[i][j]
			a=chr(z)
			original_plain += a

print(original_plain)
f1=open("original.txt","w").write(original_plain)
