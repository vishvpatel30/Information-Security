
def encrypt(x,k):
	
	p=(x + k)%128	
	ci=chr(p)
	return ci


def decrypt(x,q):
	
	p=(x - q)%128	
	ci=chr(p)
	return ci


new = ""
final = ""

a=input("Enter 1.Encrypt and 2.Decrypt : ")

if (a==1):
	k=input("Enter the key : ")
	f= open ("ex.txt")
	for i in f:
		for x in i:
			new=new + encrypt( ord(x),k)

	f1=open("new.txt","w").write(new)
	

else :
	z=input("1.Brut force or 2.Hacker or 3.Frequency : ")
	
	if(z==1):
		b=''
		q=0
		while(b!='y'):
			final = ""
			f1= open ("new.txt")
			for i in f1:
				for x in i:
					
					final=final + decrypt( ord(x),q)
			print (final)
			q=q+1
			b=raw_input("Readable y or n : ")
			
		
	
	elif(z==2) :
		q=input("Enter the key : ")
		f1= open ("new.txt")
		for i in f1:
			for x in i:
				final=final + decrypt( ord(x),q)
		print(final)
		
	else :
		newfreq={}
		freq=' etaoinsrhldcumfpgwybvkxjqz0123456789'
		f1= open ("new.txt")
		for i in f1:
			for x in i:
				if x in newfreq:
					newfreq[x] += 1
				else :
					newfreq[x] =1
		maxchar= ""
		maxcount=0		
		for i in newfreq:
			if(newfreq[i]>maxcount):
				maxcount = newfreq[i]
				maxchar = i
		print("Max char in : " + str(maxchar))
		for i in freq:
			form=ord(maxchar)
			original=ord(i)
			key=(form-original)%256
			f1=open("new.txt")
			for i in f1:
				for x in i:
					final=final + decrypt( ord(x),key)
			print(final)
			g=raw_input("If you can read than press y : ")
			if(g=='y'):
				break
			final=''
		
	f2=open("final.txt","w").write(final)
