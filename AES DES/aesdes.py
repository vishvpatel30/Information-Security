from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES,DES
from Crypto.Util.Padding import pad,unpad

plain=""
choice = int(input("1)AES\n2)DES\n"))
f=open("plain.txt","rb")
plain=f.read()

if choice == 1:#AES
    keysize = int(input("Enter key size(128  /  192  /  256): "))
    if keysize != 128 and keysize != 192 and keysize != 256:
        print("Invalid Key Size")
    key = get_random_bytes(keysize//8)

    mode = input("Enter mode(CBC  /  CFB  /  OFB  /  CTR  /  EAX  /  ECB): ")
    if mode == "CBC":

        cipher = AES.new(key, AES.MODE_CBC)
        ciphered = cipher.encrypt(pad(plain, AES.block_size))

        print(ciphered)
        f1=open("new.txt","wb")
        cipher1=f1.write(ciphered)

        f1=open("new.txt","rb")
        ciphered=f1.read()

        cipher = AES.new(key, AES.MODE_CBC, iv=cipher.iv)
        original = unpad(cipher.decrypt(ciphered), AES.block_size)
        print(original.decode())


    if mode == "CFB":
        cipher = AES.new(key, AES.MODE_CFB)
        ciphered = cipher.encrypt(plain)

        print(ciphered)
        f1=open("new.txt","wb")
        cipher1=f1.write(ciphered)


        f1=open("new.txt","rb")
        ciphered=f1.read()

        cipher = AES.new(key, AES.MODE_CFB, iv=cipher.iv)
        original = cipher.decrypt(ciphered)
        print(original.decode())


    if mode == "EAX":
        cipher = AES.new(key, AES.MODE_EAX)
        ciphered, tag = cipher.encrypt_and_digest(plain)

        print(ciphered)
        f1=open("new.txt","wb")
        cipher1=f1.write(ciphered)


        f1=open("new.txt","rb")
        ciphered=f1.read()

        cipher = AES.new(key, AES.MODE_EAX, cipher.nonce)
        original = cipher.decrypt_and_verify(ciphered, tag)
        print(original.decode())

    if mode == "CTR":
        cipher = AES.new(key, AES.MODE_CTR)
        ciphered = cipher.encrypt(plain)

        print(ciphered)
        f1=open("new.txt","wb")
        cipher1=f1.write(ciphered)

        f1=open("new.txt","rb")
        ciphered=f1.read()

        cipher = AES.new(key, AES.MODE_CTR, nonce=cipher.nonce)
        original = cipher.decrypt(ciphered)
        print(original.decode())

    if mode == "OFB":
        cipher = AES.new(key, AES.MODE_OFB)
        ciphered = cipher.encrypt(plain)

        print(ciphered)
        f1=open("new.txt","wb")
        cipher1=f1.write(ciphered)


        f1=open("new.txt","rb")
        ciphered=f1.read()

        cipher = AES.new(key, AES.MODE_OFB, iv=cipher.iv)
        original = cipher.decrypt(ciphered)
        print(original.decode())

    if mode == "ECB":
        cipher = AES.new(key, AES.MODE_ECB)
        ciphered = cipher.encrypt(pad(plain, AES.block_size))

        print(ciphered)
        f1=open("new.txt","wb")
        cipher1=f1.write(ciphered)

        f1=open("new.txt","rb")
        ciphered=f1.read()

        cipher = AES.new(key, AES.MODE_ECB)
        original = unpad(cipher.decrypt(ciphered), AES.block_size)
        print(original.decode())

#print("--------------------------------------------------------------")

if choice == 2:#AES
    key = get_random_bytes(8)

    mode = input("Enter mode(CBC  /  CFB  /  OFB  /  CTR  /  EAX  /  ECB): ")
    if mode == "CBC":

        cipher = DES.new(key, DES.MODE_CBC)
        ciphered = cipher.encrypt(pad(plain, DES.block_size))

        print(ciphered)
        f1=open("new.txt","wb")
        cipher1=f1.write(ciphered)

        f1=open("new.txt","rb")
        ciphered=f1.read()

        cipher = DES.new(key, DES.MODE_CBC, iv=cipher.iv)
        original = unpad(cipher.decrypt(ciphered), DES.block_size)
        print(original.decode())


    if mode == "CFB":
        cipher = DES.new(key, DES.MODE_CFB)
        ciphered = cipher.encrypt(plain)

        print(ciphered)
        f1=open("new.txt","wb")
        cipher1=f1.write(ciphered)


        f1=open("new.txt","rb")
        ciphered=f1.read()

        cipher = DES.new(key, DES.MODE_CFB, iv=cipher.iv)
        original = cipher.decrypt(ciphered)
        print(original.decode())

    if mode == "EAX":
        cipher = DES.new(key, DES.MODE_EAX)
        ciphered, tag = cipher.encrypt_and_digest(plain)

        print(ciphered)
        f1=open("new.txt","wb")
        cipher1=f1.write(ciphered)

        f1=open("new.txt","rb")
        ciphered=f1.read()

        cipher = DES.new(key, DES.MODE_EAX, cipher.nonce)
        original = cipher.decrypt_and_verify(ciphered, tag)
        print(original.decode())

    if mode == "CTR":
        cipher = DES.new(key, DES.MODE_CTR)
        ciphered = cipher.encrypt(plain)

        print(ciphered)
        f1=open("new.txt","wb")
        cipher1=f1.write(ciphered)

        f1=open("new.txt","rb")
        ciphered=f1.read()

        cipher = DES.new(key, DES.MODE_CTR, nonce=cipher.nonce)
        original = cipher.decrypt(ciphered)
        print(original.decode())

    if mode == "OFB":
        cipher = DES.new(key, DES.MODE_OFB)
        ciphered = cipher.encrypt(plain)

        print(ciphered)
        f1=open("new.txt","wb")
        cipher1=f1.write(ciphered)

        f1=open("new.txt","rb")
        ciphered=f1.read()

        cipher = DES.new(key, DES.MODE_OFB, iv=cipher.iv)
        original = cipher.decrypt(ciphered)
        print(original.decode())

    if mode == "ECB":
        cipher = DES.new(key, DES.MODE_ECB)
        ciphered = cipher.encrypt(pad(plain, DES.block_size))

        print(ciphered)
        f1=open("new.txt","wb")
        cipher1=f1.write(ciphered)

        f1=open("new.txt","rb")
        ciphered=f1.read()

        cipher = DES.new(key, DES.MODE_ECB)
        original = unpad(cipher.decrypt(ciphered), DES.block_size)
        print(original.decode())
