# Program to find GCD using Euclid's Algorithm

a = int(input("Enter first integer: "))#48
b = int(input("Enter second integer: "))#18

while b != 0:
    remainder = a % b
    a = b
    b = remainder

print("GCD =", abs(a))#6
