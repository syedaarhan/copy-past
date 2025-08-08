import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 6])
y = np.array([0, 250])
plt.plot(x, y)
plt.show()

x = np.array([1, 2, 6, 8])
y = np.array([3, 8, 1, 10])
plt.plot(x, y, "r--")
plt.title("Example")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid()
plt.show()

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x, y, color="red")
plt.show()

y = np.array([35, 25, 25, 15])
labels = ["Apples", "Bananas", "Mangoes", "Dates"]
plt.pie(y, labels=labels)
plt.legend()
plt.show()