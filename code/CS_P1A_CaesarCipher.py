def encrypt(text, s):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


def decrypt(text, s):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
    return result


s = 3
print("Select operation for Caesar Cipher as below:")
print("1: Encryption")
print("2: Decryption")
print("0: Exit")

while True:
    ch = int(input("\nEnter choice for operation = "))
    if ch == 1:
        text = input("Enter the secret message you want to share = ")
        print("Encrypted message is = ", encrypt(text, s))
    elif ch == 2:
        text = input("Enter the secret message you want to decrypt = ")
        print("Decrypted message is = ", decrypt(text, s))
    elif ch == 0:
        print("====== Exit ======")
        break
    else:
        print("Invalid !!!")
