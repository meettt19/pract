import rsa

public_key, private_key = rsa.newkeys(1024)
print(public_key)
print('\n', private_key)

with open("public.pem", "wb") as f:
    f.write(public_key.save_pkcs1("PEM"))

with open("private.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM"))

with open("public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

message = input("\nEnter the secrete message you want to share = ")

print('Select operation')
print('1: Confidentiality - Encryption')
print('2: Confidentiality - Decryption')
print('3: Digital Signature')
print('4: Exit')

while True:
    ch = int(input('Enter choice for operation = '))

    if ch == 1:
        encrypted_message = rsa.encrypt(message.encode(), public_key)
        decrypted_message = rsa.decrypt(encrypted_message, private_key)
        print("Decrypted message is =", decrypted_message.decode())

    elif ch == 2:
        encrypted_message = rsa.encrypt(message.encode(), public_key)
        decrypted_message = rsa.decrypt(encrypted_message, private_key)
        print("Decrypted message is =", decrypted_message.decode())

    elif ch == 3:
        digi_sign = rsa.sign(message.encode(), private_key, "SHA-256")
        print("Digital Signature is =", digi_sign)
        option = input("Do you want to verify it (y/n)")
        if option == 'y':
            print(rsa.verify(message.encode(), digi_sign, public_key))

    else:
        break


import hmac
import hashlib

def generate_mac(message, key):
    if isinstance(message, str):
        message = message.encode('utf-8')
    if isinstance(key, str):
        key = key.encode('utf-8')
    h = hmac.new(key, message, hashlib.sha256)
    return h.hexdigest()

def verify_mac(message, key, mac):
    generated_mac = generate_mac(message, key)
    return generated_mac == mac

message = input("Enter the message whose HMAC is to be generated")
key = input("Enter random Secret Key to create HMAC")

mac = generate_mac(message, key)
print("Generated MAC:", mac)

option = input("Do you want to verify it (y/n)")
if option == 'y':
    is_valid = verify_mac(message, key, mac)
    print("mac is valid :", is_valid)


from random import randint

if __name__ == '__main__':
    p = int(input("Enter the value of prime number p"))
    g = int(input("Enter the value of Generator g"))
    print('Agreed Prime is : %d ' % (p))
    print('And Agreed generator g is : %d ' % (g))
    
    a = int(input("Enter Alice's Secret Key"))
    print('Secret number for Alice is : %d ' % (a))
    PUa = int(pow(g, a, p))
    
    b = int(input("Enter Bob's Secret Key"))
    print('Secret number for Bob is : %d ' % (b))
    PUb = int(pow(g, b, p))
    
    Ka = int(pow(PUb, a, p))
    Kb = int(pow(PUa, b, p))
    
    print('Secret Key for the Alice is : %d ' % (Ka))
    print('Secret Key for the Bob is : %d ' % (Kb))

