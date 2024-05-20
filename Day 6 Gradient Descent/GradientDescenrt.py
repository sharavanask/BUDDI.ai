import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

def gradient_descent(x, y, lr=0.01, tolerance=10e-6):
    # Initial random values for coefficients
    b0 = np.random.normal(0, 1)
    b1 = np.random.normal(0, 1)
    
    # Calculate initial error
    error = np.mean((y - (b0 + b1 * np.array(x))) ** 2)
    
    # Initialize epoch, error, and coefficient history
    epoch = 0
    Epoch = [0]
    E = [error]
    Gb0 = [b0]
    Gb1 = [b1]
    
    # Loop until convergence
    while True:
    
        y_pred = b0 + b1 * np.array(x)
        db0 = -2 * np.mean(y - y_pred)
        db1 = -2 * np.mean((y - y_pred) * np.array(x))
        
        # Update coefficients
        b0 -= lr * db0
        b1 -= lr * db1
        
        # Compute new error
        new_error = np.mean((y - (b0 + b1 * np.array(x))) ** 2)
        epoch += 1
        
        # Store values for plotting and analysis
        Epoch.append(epoch)
        E.append(new_error)
        Gb0.append(b0)
        Gb1.append(b1)
        
        # Check convergence
        if abs(error - new_error) < tolerance:
            break
        else:
            error = new_error
    
    return b0, b1, E, Epoch, Gb0, Gb1

# Generating random 1000 values to be appended in x
x = []
y = []
for i in range(-500, 500):
    x_val = i / 1000
    x.append(x_val) 
    n = np.random.normal(0, 5)
    y_val = 2 * x_val - 3 + n
    y.append(y_val)

# Splitting data into training and testing sets (80-20 ratio)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

# Running gradient descent on training data
b0_finalt, b1_finalt, Et, Epocht, Gb0t, Gb1t = gradient_descent(x_train, y_train)
b0_finalt2, b1_finalt2, Et2, Epocht2, Gb0t2, Gb1t2 = gradient_descent(x_test, y_test)

# Printing final coefficients and error
print("Gradient Descent trainnig: b0:", b0_finalt, "b1:", b1_finalt)
print("Final Training Error:", Et[-1])
print("Gradient Descent trainnig: b0:", b0_finalt2, "b1:", b1_finalt2)
print("Final Training Error:", Et2[-1])
# Evaluate the model on the test set
test_error = np.mean((y_test - (b0_finalt + b1_finalt * np.array(x_test))) ** 2)
print("Test Error:", test_error)

# Plotting the error convergence
plt.figure(figsize=(8, 4))
plt.plot(Epocht, Et,label="training error")
plt.plot(Epocht2,Et2,label="testing error")
plt.xlabel('Number of Epoch Cycles')
plt.ylabel('Mean Squared Error')
plt.title('Gradient Descent')
plt.legend()
plt.figtext(0.5, 0.01, "In the above graph, the Mean Square Error is plotted with respect to the number of Epoch cycles executed", ha="center", fontsize=10, bbox={"facecolor":"brown", "alpha":0.5, "pad":5})

plt.show()