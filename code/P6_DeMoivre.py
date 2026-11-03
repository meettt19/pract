import cmath
import math

a = float(input("Enter real part: "))
b = float(input("Enter imaginary part: "))
n = float(input("Enter power n: "))

z = complex(a, b)

r = abs(z)
theta = cmath.phase(z)

# De Moivre's theorem
result = (r ** n) * (
    math.cos(n * theta) + 1j * math.sin(n * theta)
)

print("\nComplex number z =",z)
print("Modulus r =", r)
print("Argument theta =", math.degrees(theta), "degrees")

print("\nUsing De Moivre's theorem:")
print("z^n =", result)

print("\nDirect Python calculation:")
print("z^n =", z ** n)
