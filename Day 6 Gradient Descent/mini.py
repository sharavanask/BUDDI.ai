import numpy as np
import matplotlib.pyplot as plt

# Generating random 1000 values to be appended in x
x = []
# array to store calculated y values
y = []
# x matrix to get squared values for calculation of beta values
x1 = [[1] * 1000, []]
# iterating each of the 100 values to calculate actual output
for i in range(-500, 500):
    x_val = i / 1000
    x.append(x_val)
    x1[1].append(i)
    n = np.random.normal(0, 5)
    y_val = 2 * x_val - 3 + n
    y.append(y_val)

# getting transpose of matrix to get closed form values
X1 = np.transpose(x1)
Y1 = np.transpose(y)

# Calculate coefficients using matrix multiplication
b = np.matmul(np.linalg.inv(np.matmul(x1, X1)), np.matmul(x1, Y1))
B0 = b[0]
B1 = b[1]

# Gradient Descent processing
b0f = np.random.normal(0, 1)
b1f = np.random.normal(0, 1)

# calculating error function
errorf = np.mean((y - (b0f + b1f * np.array(x))) ** 2)
lr = 0.01

# finding error values for initial b0 and b1 values
error = errorf
b0 = b0f
b1 = b1f
epoch = 0

# initializing epoch matrix
Epoch = [0]
E = [errorf]

# array to store gradient b0 and b1 value
Gb0 = []
Gb1 = []

out = False

# splitting the dataset into minibatches
num_minibatches = 20
minibatch_size = 50
minibatches = np.array_split(x, num_minibatches)

# updating epoch values until the error is close to near 0 values
while not out:
    for minibatch in minibatches:
        # calculating gradients for the current minibatch
        grad_b0 = 0
        grad_b1 = 0
        for i in range(len(minibatch)):
            grad_b0 += -2 * ((y[i] - b0 + b1 * minibatch[i]) * minibatch[i])
            grad_b1 += -2 * ((y[i] - b0 + b1 * minibatch[i]) * minibatch[i])
        grad_b0 /= len(minibatch)
        grad_b1 /= len(minibatch)
        
        # updating new b0 and b1 values
        b0 -= lr * grad_b0
        b1 -= lr * grad_b1
        
        # computing error for new b0 and b1 values
        ne = (y - (b0 + b1 * np.array(x))) ** 2
        new_error = np.mean(ne)
        
        epoch += 1
        # appending epoch values
        Epoch.append(epoch)
        E.append(new_error)
        Gb0.append(b0)
        Gb1.append(b1)
        
        # checking stop condition
        if abs(error - new_error) < 10e-6:
            out = True
        else:
            error = new_error

print("Closed Form: b0:", B0, "b1:", B1, "error:", errorf)
print("Minibatch Gradient Descent: b0:", b0, "b1:", b1, "error:", error, "epoch:", epoch)

# Plotting the error convergence
plt.figure(figsize=(8, 4))
plt.plot(Epoch, E, label="MSE")
plt.xlabel('Number of Epoch Cycles')
plt.ylabel('Mean Squared Error')
plt.title('Minibatch Gradient Descent')
plt.legend()
plt.figtext(0.5, 0.01, "In the above graph the Mean Square Error is plotted with respect to the number of Epoch cycle is executed", ha="center", fontsize=10, bbox={"facecolor": "brown", "alpha": 0.5, "pad": 5})
plt.show()
