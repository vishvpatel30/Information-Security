plain=''
f=open("example.txt")
for i in f:
    for j in i:
        plain+=j

print("1.Encrypt:  2.Decrypt:")
m=int(input("Enter number:"))
if(m==1):
	l=len(plain)
	k=int(input("Enter key:"))
	et=""
	for j in range(0,k):
		if(j==0):
			i=0
			while((2*i*(k-1))<l):
				et+=plain[(2*i*(k-1))]
				i+=1
		if(j>0 and j<(k-1)):
			i=0
			while(((2*i*(k-1))+j)<l):
				if(((2*(i+1)*(k-1))-j)>=l):
					et+=plain[(2*i*(k-1))+j]
					i+=1
				else:
					et+=plain[(2*i*(k-1))+j]+plain[(2*(i+1)*(k-1))-j]
					i+=1
		if(j==(k-1)):
			i=0
			while((2*i*(k-1)+j)<l):
				et+=plain[(2*i*(k-1))+j]
				i+=1
	print(et)
	f1=open("new.txt","w").write(et)

else:
	enc=''
	f=open("new.txt")
	for i in f:
		for j in i:
			enc+=j
	li=[]
	for i in range(len(enc)):
		li.append(" ")
	l=len(enc)
	k=int(input("Enter key:"))
	z=0
	for j in range(0,k):
		if(j==0):
			i=0			
			while((2*i*(k-1))<l):
				li[2*i*(k-1)]=enc[z]
				z+=1
				i+=1
		if(j>0 and j<(k-1)):
			i=0			
			while(((2*i*(k-1))+j)<l):
				if(((2*(i+1)*(k-1))-j)>=l):
					li[(2*i*(k-1))+j]=enc[z]
					z+=1						
					i+=1
				else:
					li[(2*i*(k-1))+j]=enc[z]
					li[(2*(i+1)*(k-1))-j]=enc[z+1]
					z+=2
					i+=1
		if(j==(k-1)):
			i=0			
			while((2*i*(k-1)+j)<l):
				li[(2*i*(k-1))+j]=enc[z]
				i+=1
				z+=1
	original=''
	for i in li:
		original+=i
	print(original)
	f2=open("original.txt","w").write(original)
