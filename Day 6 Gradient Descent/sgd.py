#STOCHASTIC GRADIENT DESCENT
#importing modules
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
# import tensorflow as tf
# Generating random 1000 vlaues to be appended in x
x = []
# array to store calculated y values
y = []
#x matrix to get squared valuies for calculation of beta values 
x1=[[1]*1000,[]]
#iterating each of the 100 values to caluclate actual output 
for i in range(-500, 500):
    x_val = i / 1000
    x.append(x_val)
    x1[1].append(i)
    n = np.random.normal(0, 5)
    y_val = 2 * x_val - 3 + n
    y.append(y_val)
#getting tranpose of matrix to get closedform values
X1=np.transpose(x1)
Y1=np.transpose(y)
# Calculate coefficients using matrix multiplication/
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.20,random_state=42)
b=np.matmul(np.linalg.inv(np.matmul(x1,X1)),np.matmul(x1,Y1))
B0=b[0]
B1=b[1]

# Gradient Descent processing'
def stochasticdescent(x,y):
    b0f = np.random.normal(0, 1)
    b1f = np.random.normal(0, 1)
    #calculating error function
    errorf = np.mean((y - (b0f + b1f*np.array(x)))**2)
    lr = 0.01
    #finding errro values for initial b0 and b1 values
    error = errorf
    b0 = b0f
    b1 = b1f
    epoch = 0
    #initialising epoch matrix
    Epoch = [0]
    # Epoch.append(0)
    E = []
    E.append(errorf)
    #array rto store gradient b0 and b1 value
    Gb0=[]
    Gb1=[]
    out = False
    #updatin epoch valiues until the the error is close to near 0 values
    while not out:
        y_pred = b0 + b1*np.array(x)
        grad_b0=0
        grad_b1=0
        # grad_b0 = -2*np.mean((y - y_pred))
        # grad_b1 = -2*np.mean((y - y_pred)*np.array(x))
        #updating beta values on each valuies as in stochastic
        for i in range(len(x)):
            grad_b0=(-2*((ytrain[i] - b0 + b1*x[i])))
            grad_b1=(-2*((ytrain[i] - b0+b1*(x[i]))*x[i]))
        # grad_b0=sum(db0)/len(db0)
        # grad_b1=sum(db1)/len(db1)
        #cupdating new b0 and b1 values
            b0 -= lr * grad_b0
            b1 -= lr * grad_b1
            # new_error = np.mean((y - (b0 + b1*np.array(x)))**2)
            ne=[]
            #computingh error for new b0 and b1 values
            for i in range(len(x)):
                ne.append((y[i] - (b0 + b1*(x[i])))**2)
            new_error = sum(ne)/len(ne)
            epoch += 1
            #appending epoch values
            Epoch.append(epoch)
            E.append(new_error)
            Gb0.append(b0)
            Gb1.append(b1)
        #cheking stop condition 
        if abs(error - new_error) < 10e-6:
            out = True
        else:
            error = new_error
        return Gb0,Gb1,E,Epoch
    
gradb0t,gradb1t,Et,Epocht=stochasticdescent(xtrain,ytrain)
gradb0t2,gradb1t2,Et2,Epocht2=stochasticdescent(xtest,ytest)
#printing  the epoch and beta values 
print("Closed Form: b0:", B0, "b1:", B1, "error:")
print("Gradient Descent: b0:",np.mean(gradb0t), "b1:", np.mean(gradb1t), "error:",np.mean(Et), "epoch:",Epocht[-1])
print("Gradient Descent: b0:",np.mean(gradb0t2), "b1:", np.mean(gradb1t2), "error:", np.mean(Et2), "epoch:",Epocht2[-1])





# Plotting the error convergence
plt.figure(figsize=(8, 4))
plt.plot(Epocht, Et,label="training error ",color="purple")
plt.plot(Epocht2, Et2,label="testing error")

plt.xlabel('NUmber of Epoch Cycles')
plt.ylabel('Mean Squared Error')
plt.title('SGD-STOCHASTIC GRADIENT DESCENT')
plt.legend()
plt.figtext(0.5, 0.01, "Let us consider a 1000 points in which the gradient is find out by using stochastic gradeint descent by  updating the beta vallues for each value wise to get a eratic graph", ha="center", fontsize=10, bbox={"facecolor":"yellow", "alpha":0.5, "pad":5})
plt.show()
#plotting the beta 1 and beta0 values with respect to epoch values
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_trisurf(Gb0,Gb1,Epoch, cmap='viridis',edgecolor='none',label = "epoc")
# ax.set_xlabel('Beta0(B0)')
# ax.set_ylabel('Beta1(B1)')
# ax.set_zlabel('Epoc')
# plt.legend()
# ax.set_title('Surface Plot')
#plotting errror function vs beta0 and beta 1
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_trisurf(Gb0,Gb1,E, cmap='viridis',edgecolor='none')
# ax.set_xlabel('Beta0(B0)')
# ax.set_ylabel('Beta1(B1)')
# ax.set_zlabel('Error')
# ax.set_title('Surface Plot')
# plt.show()