import matplotlib.pyplot as plt

n = range(1, 101)

sequence = [1/i for i in n]

print("First 10 terms:")
print(sequence[:10])

plt.plot(n, sequence, marker='o')
plt.axhline(y=0, linestyle='--')
plt.xlabel("n")
plt.ylabel("a(n)")
plt.title("Convergence of Sequence a(n) = 1/n")
plt.grid()
plt.show()
