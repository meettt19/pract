a = int(input("Enter first integer: ")) #6
b = int(input("Enter second integer: ")) #2

x = a
y = b
while y != 0:
    x, y = y, x % y

gcd = abs(x)

if a == 0 or b == 0:
    lcm = 0
else:
    lcm = abs(a * b)
print("LCM =", lcm)
