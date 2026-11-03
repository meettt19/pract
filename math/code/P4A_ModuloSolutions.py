import math

a = int(input("Enter a: "))#5
b = int(input("Enter b: "))#7
m = int(input("Enter modulus m: "))#12

solutions = []

for x in range(m):
    if (a * x - b) % m == 0:
        solutions.append(x)

if len(solutions) == 0:
    print("No solution exists.")
else:
    print("Solutions modulo", m, "are:", solutions)
