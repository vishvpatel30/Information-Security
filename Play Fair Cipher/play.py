import numpy as num
def mat(m,a):
	for i in range(6):
		for j in range(6):
			if (m[i][j]==a):
				return i,j


def encrypt(x,y,z):
	row1,column1=mat(x,y)
	row2,column2=mat(x,z)
	if (row1==row2):
		column1=(column1+1)%6
		column2=(column2+1)%6
	elif (column1==column2):
		row1=(row1+1)%6
		row2=(row2+1)%6
	else :
		ab=column1
		column1=column2
		column2=ab
	return x[row1][column1],x[row2][column2]

def decrypt(x,y,z):
	row1,column1=mat(x,y)
	row2,column2=mat(x,z)
	if (row1==row2):
		column1=(column1-1)%6
		column2=(column2-1)%6
	elif (column1==column2):
		row1=(row1-1)%6
		row2=(row2-1)%6
	else :
		ab=column1
		column1=column2
		column2=ab
	return x[row1][column1],x[row2][column2]


extra="abcdefghijklmnopqrstuvwxyz0123456789"
k=raw_input("Enter the Key")
key=''
for i in k:
	if (i.isupper()):
		i=i.lower()
	if (i.isalnum()):
		key+=i

dup=''
for i in key:
	dup+=i
for j in extra:
	dup+=j

org=''
for i in dup:
	if i not in org:
		org+=i

matrix=num.chararray((6,6))
a=0
while(a<36):
	for i in range(6):
		for j in  range(6):
			matrix[i][j]=org[a]
			a+=1
print(matrix)


abc=''
f=open("abc.txt")
for i in f:
	for j in i:
		if(j.isalnum()):
			if (j.isupper()):
				j=j.lower()
			abc+=j
if (len(abc)%2==0):
	abc+='z'

xyz=''
for i in range(0,len(abc)-1,2):
	if (abc[i]==abc[i+1]):
		xyz+=abc[i]+'x'+abc[i+1]
	else:
		xyz=xyz+abc[i]+abc[i+1]

original=''
new1=''
new2=''
for i in range(0,len(xyz)-1,2):
	x=xyz[i]
	y=xyz[i+1]
	p,q=encrypt(matrix,x,y)
	new1+=p
	new2+=q


for i in range(0,len(new1)):
	original+=new1[i]+new2[i]
print("Cipher text is:")
print(original)

print(" ")




plain=''
pla1=''
pla2=''
for i in range(0,len(original)-1,2):
	x=original[i]
	y=original[i+1]
	p,q=decrypt(matrix,x,y)
	pla1+=p
	pla2+=q

for i in range(0,len(pla1)):
	plain+=pla1[i]+pla2[i]
print("Plain text:")
print(plain)



















