#same mean
import numpy as np
import matplotlib.pyplot as plt
m = 2
sd = 1
x = np.linspace(m-(5*sd),m  +(5*sd))
print(x)
f = (1 / (sd * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - m) / sd) ** 2)
plt.plot(x, f, color='blue', label='Normal Distribution')
sd1 = 2
x = np.linspace(m-(5*sd1),m  +(5*sd1))
f = (1 / (sd1 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - m) / sd1) ** 2)
plt.plot(x, f, color='yellow', label='Normal Distribution')
sd2 = 3
x = np.linspace(m-(5*sd2),m  +(5*sd2))
f = (1 / (sd2 * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - m) / sd2) ** 2)
plt.plot(x, f, color='purple', label='Normal Distribution')
plt.title("Normal Distribution (Constant Mean)")
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)
plt.figtext(0.5, 0.01, "Plotting a normal Distribution graph by using its equation,keeping mean as constant and standard deviation as changing", ha="center", fontsize=10, bbox={"facecolor":"brown", "alpha":0.5, "pad":5})
plt.show()



