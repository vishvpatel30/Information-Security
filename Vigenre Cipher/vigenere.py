
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