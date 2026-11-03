#Practical 5b: Convert Complex Number from Cartesian Form to Polar Form

import cmath
import math

x = float(input("Enter real part:"))
y = float(input("Enter imaginary part:"))

z = complex(x,y)

r, theta = cmath.polar(z)

theta_degree = math.degrees(theta)

print("Complex number =", z)
print("Modulus (r) =",r)
print("Argument (theta) in radians =", theta)
print("Argument (theta) in degrees =", theta_degree)

print("\nPolar form:")
print(f"{r:.2}(cos({theta_degree:.2f}°) + i sin({theta_degree:.2f}°))")
