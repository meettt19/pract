# Properties of Congruence

a = int(input("Enter a: ")) #17
b = int(input("Enter b: ")) #5
c = int(input("Enter c: ")) #29
m = int(input("Enter modulus: ")) #12

print("\n--- Properties of Congruence ---")

#Reflexive
if (a - a) % m == 0:
    print("1. Reflexive property: True")

#Symmetric
if (a - a) % m == 0:
    print("2. Symmetric property: True")
    
#Transitive
if (a - a) % m == 0 and (b - c) % m == 0:
   print("3. Transitive property: True")

#Addition
if (a - b) % m == 0 :
    if (a + c -(b + c)) % m == 0:
        print("4. Addition property: True")

#Subtraction
if (a - b) % m == 0 :
    if (a - c -(b - c)) % m == 0:
        print("5. Subtraction property: True")

#Multiplication
if (a - b) % m == 0 :
    if (a * c - b * c) % m == 0:
        print("6. Multiplication property: True")

#Power
n = int(input("Enter power n: ")) #2

if (a - b) % m == 0 :
    if (a ** n - b ** n) % m == 0:
        print("7. Power property: True")
