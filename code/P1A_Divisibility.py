a = int(input("Enter first integer: ")) #6
b = int(input("Enter second integer: ")) #2

if b != 0:
    if a % b == 0:
        print(a, "is divisible by", b)
    else:
        print(a, "is not divisible by", b)

else:
    print("Division by Zero is not allowed")
