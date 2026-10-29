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
