import matplotlib.pyplot as plt

x = list(range(-10, 11))
y = [-(xi**2) for xi in x]
y1 = [xi**2 for xi in x]
plt.plot(x, y, label="y=-x^2")
plt.plot(x, y1, label="y=x^2")
plt.show()
