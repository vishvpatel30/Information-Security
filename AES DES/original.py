from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES,DES
from Crypto.Util import Counter
from Crypto.Util.Padding import pad,unpad
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from phe import paillier


output_file = "IS\encrypted.bin"
input_file = "IS\Plain.txt"
output_file = "IS\encrypted.bin"

cipher = int(input("1)AES\n2)DES\n3)RSA\n4)Paillier\n"))

if cipher == 1:#AES
    key_size = int(input("Enter key size(128/192/256): "))
    if key_size != 128 and key_size != 192 and key_size != 256:
        print("Invalid Key Size")
    key = get_random_bytes(key_size//8)

    mode = input("Enter mode(CBC/CFB/OFB/CTR/EAX/ECB): ")
    if mode == "CBC":
        input_file = open(input_file,"rb")
        data = input_file.read()
        input_file.close()

        cipher = AES.new(key, AES.MODE_CBC)
        ciphered_data = cipher.encrypt(pad(data, AES.block_size))

        file_out = open(output_file, "wb")
        file_out.write(ciphered_data)
        file_out.close()
        print("Data Encryption Successful")

        input_file = open(output_file, "rb")
        ciphered_data = input_file.read()
        input_file.close()

        cipher = AES.new(key, AES.MODE_CBC, iv=cipher.iv)
        original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size)
        print(original_data.decode())
        print("Data Decryption Successful")

    elif mode == "CFB":
        input_file = open(input_file, "rb")
        data = input_file.read()
        input_file.close()

        cipher = AES.new(key, AES.MODE_CFB)
        ciphered_data = cipher.encrypt(data)

        file_out = open(output_file, "wb")
        file_out.write(ciphered_data)
        file_out.close()
        print("Data Encryption Successful")

        input_file = open(output_file, "rb")
        ciphered_data = input_file.read()
        input_file.close()

        cipher = AES.new(key, AES.MODE_CFB, iv=cipher.iv)
        original_data = cipher.decrypt(ciphered_data)
        print(original_data.decode())
        print("Data Decryption Successful")

    elif mode == "EAX":
        input_file = open(input_file, "rb")
        data = input_file.read()
        input_file.close()

        cipher = AES.new(key, AES.MODE_EAX)
        ciphered_data, tag = cipher.encrypt_and_digest(data)

        file_out = open(output_file, "wb")
        file_out.write(ciphered_data)
        file_out.close()
        print("Data Encryption Successful")

        input_file = open(output_file, "rb")
        ciphered_data = input_file.read()
        input_file.close()

        cipher = AES.new(key, AES.MODE_EAX, cipher.nonce)
        original_data = cipher.decrypt_and_verify(ciphered_data, tag)
        print(original_data.decode())
        print("Data Decryption Successful")

    elif mode == "OFB":
        input_file = open(input_file, "rb")
        data = input_file.read()
        input_file.close()

        cipher = AES.new(key, AES.MODE_OFB)
        ciphered_data = cipher.encrypt(data)

        file_out = open(output_file, "wb")
        file_out.write(ciphered_data)
        file_out.close()
        print("Data Encryption Successful")

        input_file = open(output_file, "rb")
        ciphered_data = input_file.read()
        input_file.close()

        cipher = AES.new(key, AES.MODE_OFB, iv=cipher.iv)
        original_data = cipher.decrypt(ciphered_data)
        print(original_data.decode())
        print("Data Decryption Successful")

    elif mode == "CTR":
        input_file = open(input_file, "rb")
        data = input_file.read()
        input_file.close()

        cipher = AES.new(key, AES.MODE_CTR)
        ciphered_data = cipher.encrypt(data)

        file_out = open(output_file, "wb")
        file_out.write(ciphered_data)
        file_out.close()
        print("Data Encryption Successful")

        input_file = open(output_file, "rb")
        ciphered_data = input_file.read()
        input_file.close()

        cipher = AES.new(key, AES.MODE_CTR, nonce=cipher.nonce)
        original_data = cipher.decrypt(ciphered_data)
        print(original_data.decode())
        print("Data Decryption Successful")

    elif mode == "ECB":
        input_file = open(input_file, "rb")
        data = input_file.read()
        input_file.close()

        cipher = AES.new(key, AES.MODE_ECB)
        ciphered_data = cipher.encrypt(pad(data, AES.block_size))

        file_out = open(output_file, "wb")
        file_out.write(ciphered_data)
        file_out.close()
        print("Data Encryption Successful")

        input_file = open(output_file, "rb")
        ciphered_data = input_file.read()
        input_file.close()

        cipher = AES.new(key, AES.MODE_ECB)
        original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size)
        print(original_data.decode())
        print("Data Decryption Successful")

    else:
        print("Invalid mode")

elif cipher == 2:#DES
    key = get_random_bytes(8)

    mode = input("Enter mode(CBC/CFB/OFB/CTR/EAX/ECB): ")
    if mode == "CBC":
        input_file = open(input_file, "rb")
        data = input_file.read()
        input_file.close()

        cipher = DES.new(key, DES.MODE_CBC)
        ciphered_data = cipher.encrypt(pad(data, DES.block_size))

        file_out = open(output_file, "wb")
        file_out.write(ciphered_data)
        file_out.close()
        print("Data Encryption Successful")

        input_file = open(output_file, "rb")
        ciphered_data = input_file.read()
        input_file.close()

        cipher = DES.new(key, DES.MODE_CBC, iv=cipher.iv)
        original_data = unpad(cipher.decrypt(ciphered_data), DES.block_size)
        print(original_data.decode())
        print("Data Decryption Successful")

    elif mode == "CFB":
        input_file = open(input_file, "rb")
        data = input_file.read()
        input_file.close()

        cipher = DES.new(key, DES.MODE_CFB)
        ciphered_data = cipher.encrypt(data)

        file_out = open(output_file, "wb")
        file_out.write(ciphered_data)
        file_out.close()
        print("Data Encryption Successful")

        input_file = open(output_file, "rb")
        ciphered_data = input_file.read()
        input_file.close()

        cipher = DES.new(key, DES.MODE_CFB, iv=cipher.iv)
        original_data = cipher.decrypt(ciphered_data)
        print(original_data.decode())
        print("Data Decryption Successful")

    elif mode == "EAX":
        input_file = open(input_file, "rb")
        data = input_file.read()
        input_file.close()

        cipher = DES.new(key, DES.MODE_EAX)
        ciphered_data, tag = cipher.encrypt_and_digest(data)

        file_out = open(output_file, "wb")
        file_out.write(ciphered_data)
        file_out.close()
        print("Data Encryption Successful")

        input_file = open(output_file, "rb")
        ciphered_data = input_file.read()
        input_file.close()

        cipher = DES.new(key, DES.MODE_EAX, cipher.nonce)
        original_data = cipher.decrypt_and_verify(ciphered_data, tag)
        print(original_data.decode())
        print("Data Decryption Successful")

    elif mode == "OFB":
        input_file = open(input_file, "rb")
        data = input_file.read()
        input_file.close()

        cipher = DES.new(key, DES.MODE_OFB)
        ciphered_data = cipher.encrypt(data)

        file_out = open(output_file, "wb")
        file_out.write(ciphered_data)
        file_out.close()
        print("Data Encryption Successful")

        input_file = open(output_file, "rb")
        ciphered_data = input_file.read()
        input_file.close()

        cipher = DES.new(key, DES.MODE_OFB, iv=cipher.iv)
        original_data = cipher.decrypt(ciphered_data)
        print(original_data.decode())
        print("Data Decryption Successful")

    elif mode == "CTR":
        counter = Counter.new(64)
        input_file = open(input_file, "rb")
        data = input_file.read()
        input_file.close()

        cipher = DES.new(key, DES.MODE_CTR, counter=counter)
        ciphered_data = cipher.encrypt(data)

        file_out = open(output_file, "wb")
        file_out.write(ciphered_data)
        file_out.close()
        print("Data Encryption Successful")

        input_file = open(output_file, "rb")
        ciphered_data = input_file.read()
        input_file.close()

        cipher = DES.new(key, DES.MODE_CTR, counter=counter)
        original_data = cipher.decrypt(ciphered_data)
        print(original_data.decode())
        print("Data Decryption Successful")

    elif mode == "ECB":
        input_file = open(input_file, "rb")
        data = input_file.read()
        input_file.close()

        cipher = DES.new(key, DES.MODE_ECB)
        ciphered_data = cipher.encrypt(pad(data, DES.block_size))

        file_out = open(output_file, "wb")
        file_out.write(ciphered_data)
        file_out.close()
        print("Data Encryption Successful")

        input_file = open(output_file, "rb")
        ciphered_data = input_file.read()
        input_file.close()

        cipher = DES.new(key, DES.MODE_ECB)
        original_data = unpad(cipher.decrypt(ciphered_data), DES.block_size)
        print(original_data.decode())
        print("Data Decryption Successful")

    else:
        print("Invalid mode")


elif cipher == 3:#RSA
    input_file = open(input_file, "rb")
    data = input_file.read()
    input_file.close()

    privateKey = RSA.generate(4096)
    publicKey = privateKey.publickey()

    cipher = PKCS1_OAEP.new(publicKey)
    ciphered_data = cipher.encrypt(data)

    file_out = open(output_file, "wb")
    file_out.write(ciphered_data)
    file_out.close()
    print("Data Encryption Successful")

    input_file = open(output_file, "rb")
    ciphered_data = input_file.read()
    input_file.close()

    cipher = PKCS1_OAEP.new(privateKey)
    original_data = cipher.decrypt(ciphered_data)
    print(original_data.decode())
    print("Data Decryption Successful")

elif cipher == 4:#Paillier
    input_file = open(input_file, "r")
    data = input_file.read()
    input_file.close()

    publicKey, privateKey = paillier.generate_paillier_keypair()
    ciphered_data = [publicKey.encrypt(ord(i)) for i in data]
    print("Data Encryption Successful")

    original_data = "".join([chr(privateKey.decrypt(i)) for i in ciphered_data])
    print(original_data)
    print("Data Decryption Successful")


else:
    print("Invalid Cipher Option")


