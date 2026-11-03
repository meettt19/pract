import matplotlib.pyplot as plt

n = 10

sequence = []

for i in range(1, n + 1):
    sequence.append(i ** 2)

print("Square Sequence:")
print(sequence)

plt.plot(range(1, n + 1), sequence, marker='o')
plt.xlabel("n")
plt.ylabel("n")
plt.title("Sequence of Square")
plt.grid()
plt.show()
