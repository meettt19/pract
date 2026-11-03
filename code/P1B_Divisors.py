n = int(input("Enter a positive integer: ")) #6

print("Divisor of", n, "are:")

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
