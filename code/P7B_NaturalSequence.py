import matplotlib.pyplot as plt

n = 10

sequence = list(range(1, n + 1))

print("Natural Number Sequence:")
print(sequence)

# Plot
plt.plot(range(1, n + 1), sequence, marker='o')
plt.xlabel("n")
plt.ylabel("a(n)")
plt.title("Natural Number Sequence")
plt.grid()
plt.show()
