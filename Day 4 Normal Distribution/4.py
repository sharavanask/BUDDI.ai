#same standard deviation
import numpy as np
import matplotlib.pyplot as plt
m = 1
sd = 1
x = np.linspace(m-(5*sd),m  +(5*sd))
f = (1 / (sd * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - m) / sd) ** 2)
plt.plot(x, f, color='yellow',label='Normal Distribution')
m2=2
x = np.linspace(m2-(5*sd),m2+(5*sd))
f = (1 / (sd * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - m2) / sd) ** 2)
plt.plot(x, f, color='blue',label='Normal Distribution')
m1 = 3
x = np.linspace(m1-(5*sd),m1  +(5*sd))
f = (1 / (sd * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - m1) / sd) ** 2)
print(x)
#plt.plot
plt.plot(x, f, color='purple', label='Normal Distribution')
plt.title("Normal Distribution (Constant Standard Deviation)")
plt.xlabel("Value")
plt.ylabel("Probability Density")
plt.legend()
plt.figtext(0.5, 0.01, "Plotting a normal Distribution graph by using its equation,keeping Standard Deviation(σ) as constant and Mean(μ) as changing", ha="center", fontsize=10, bbox={"facecolor":"brown", "alpha":0.5, "pad":5})
plt.show()



