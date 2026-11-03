a = int(input("Enter first integer: ")) #6
b = int(input("Enter second integer: ")) #2

print("Common Divisors are:")

for i in range(1, min(abs(a), abs(b)) + 1):
    if a % i == 0 and b % i == 0:
        print(i, end=" ")
